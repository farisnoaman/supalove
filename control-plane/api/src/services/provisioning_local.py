import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Decoupled Configuration
# In a real app, these should be loaded from os.environ or a config module
# For now, we default to the relative path but allow override via env var
# Determine PROJECT_ROOT safely for both Local and Docker environments
try:
    PROJECT_ROOT = Path(__file__).resolve().parents[4]  # Local: .../supalove/
except IndexError:
    PROJECT_ROOT = Path(__file__).resolve().parents[2]  # Docker: /app

env_projects_dir = os.getenv("DATA_PLANE_BASE_DIR")
if env_projects_dir:
    BASE_PROJECTS_DIR = Path(env_projects_dir)
else:
    BASE_PROJECTS_DIR = PROJECT_ROOT / "data-plane" / "projects"
    
TEMPLATE_DIR_NAME = "project-template"

from services.provisioning_interface import Provisioner

class LocalProvisioner(Provisioner):
    """Local Docker Compose based provisioner"""

    def __init__(self):
        # Locate project root from this file
        self.project_root = PROJECT_ROOT
    
    def provision(self, project_id: str, secrets: Optional[dict] = None, custom_domain: Optional[str] = None) -> Dict[str, Any]:
        """Provisions a new project using local Docker Compose scripts."""
        if secrets is None:
            secrets = {}

        # Get the assigned ports from secrets
        db_port = secrets.get("DB_PORT", "5432")
        rest_port = secrets.get("REST_PORT", "3000")
        realtime_port = secrets.get("REALTIME_PORT", "5433")
        db_password = secrets.get("DB_PASSWORD", "postgres")

        # Create project directory
        project_dir = BASE_PROJECTS_DIR / project_id
        project_dir.mkdir(exist_ok=True, parents=True)

        # Copy project template
        template_dir = PROJECT_ROOT / "data-plane" / "project-template"
        if not template_dir.exists():
            # DEBUG LOGGING FOR DEPLOYMENT
            print(f"DEBUG: PROJECT_ROOT = {PROJECT_ROOT}")
            print(f"DEBUG: CWD = {os.getcwd()}")
            print(f"DEBUG: Contents of PROJECT_ROOT ({PROJECT_ROOT}):")
            try:
                for p in PROJECT_ROOT.iterdir():
                    print(f" - {p}")
            except Exception as e:
                print(f" Error listing PROJECT_ROOT: {e}")
            
            print(f"DEBUG: Checking {PROJECT_ROOT / 'data-plane'}:")
            try:
                if (PROJECT_ROOT / 'data-plane').exists():
                    print(" 'data-plane' exists. Contents:")
                    for p in (PROJECT_ROOT / 'data-plane').iterdir():
                        print(f" - {p}")
                else:
                    print(" 'data-plane' DOES NOT EXIST.")
            except Exception as e:
                print(f" Error listing data-plane: {e}")

            raise FileNotFoundError(f"Project template not found at {template_dir}")

        # Copy all files from template to project directory
        import shutil
        for item in template_dir.iterdir():
            if item.is_file():
                shutil.copy2(item, project_dir)
            elif item.is_dir():
                shutil.copytree(item, project_dir / item.name, dirs_exist_ok=True)

        # Create .env file for the project
        env_content = f"# Project: {project_id}\n"
        # Always inject PROJECT_ID for docker network isolation
        env_content += f"PROJECT_ID={project_id}\n"
        for key, value in secrets.items():
            env_content += f"{key}={value}\n"
            
        env_file = project_dir / ".env"
        env_file.write_text(env_content)

        # Start the Docker containers
        import subprocess
        try:
            result = subprocess.run(
                ["docker", "compose", "up", "-d"],
                cwd=project_dir,
                capture_output=True,
                text=True,
                timeout=300  # Increased from 60s to 300s to allow image pull
            )

            if result.returncode != 0:
                print(f"Failed to start containers: {result.stderr}")
                raise Exception(f"Docker compose failed: {result.stderr}")

            print(f"Successfully provisioned project {project_id} on ports: DB={db_port}, REST={rest_port}")

        except subprocess.TimeoutExpired:
            raise Exception("Docker compose startup timed out")
        except Exception as e:
            # Clean up on failure
            # try:
            #     subprocess.run(["docker", "compose", "down"], cwd=project_dir, capture_output=True)
            # except:
            #     pass
            raise e

        return {
            "api_url": f"http://localhost:{rest_port}",
            "db_url": f"postgresql://app:{db_password}@localhost:{db_port}/app",
            "realtime_url": f"ws://localhost:{realtime_port}"
        }

    def stop(self, project_id: str) -> None:
        project_dir = BASE_PROJECTS_DIR / project_id
        if project_dir.exists():
            import subprocess
            subprocess.run(["docker", "compose", "stop"], cwd=project_dir, capture_output=True)

    def start(self, project_id: str) -> None:
        project_dir = BASE_PROJECTS_DIR / project_id
        if project_dir.exists():
            import subprocess
            subprocess.run(["docker", "compose", "start"], cwd=project_dir, capture_output=True)

    def destroy(self, project_id: str) -> None:
        project_dir = BASE_PROJECTS_DIR / project_id
        if project_dir.exists():
            import subprocess
            subprocess.run(["docker", "compose", "down", "-v"], cwd=project_dir, capture_output=True)
            import shutil
            shutil.rmtree(project_dir)

    def restore(self, project_id: str) -> None:
        project_dir = BASE_PROJECTS_DIR / project_id
        if project_dir.exists():
            import subprocess
            subprocess.run(["docker", "compose", "up", "-d"], cwd=project_dir, capture_output=True)
