import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Adjust path to find scripts
PROJECT_ROOT = Path(__file__).resolve().parents[4]
sys.path.append(str(PROJECT_ROOT))

# TODO: Import script functions when scripts are implemented
# from scripts.provision_project import provision_project as script_provision
# from scripts.lifecycle import (
#     stop_project as script_stop,
#     start_project as script_start,
#     delete_project as script_delete,
#     restore_project as script_restore,
# )
from services.provisioning_interface import ProvisioningProvider

BASE_PROJECTS_DIR = PROJECT_ROOT / "data-plane" / "projects"

class LocalProvisioner(ProvisioningProvider):
    """Local Docker Compose based provisioner"""

    def __init__(self):
        # Locate project root from this file
        self.project_root = Path(__file__).resolve().parents[4]
    
    def provision_project(self, project_id: str, secrets: Optional[dict] = None) -> Dict[str, Any]:
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
        project_dir.mkdir(exist_ok=True)

        # Copy project template
        template_dir = PROJECT_ROOT / "data-plane" / "project-template"
        if not template_dir.exists():
            raise FileNotFoundError(f"Project template not found at {template_dir}")

        # Copy all files from template to project directory
        import shutil
        for item in template_dir.iterdir():
            if item.is_file():
                shutil.copy2(item, project_dir)
            elif item.is_dir():
                shutil.copytree(item, project_dir / item.name, dirs_exist_ok=True)

        # Create .env file for the project
        env_content = f"""# Project: {project_id}
DB_PASSWORD={db_password}
DB_PORT={db_port}
REST_PORT={rest_port}
REALTIME_PORT={realtime_port}
JWT_SECRET={secrets.get('JWT_SECRET', 'default-jwt-secret')}
ANON_KEY={secrets.get('ANON_KEY', 'default-anon-key')}
SERVICE_ROLE_KEY={secrets.get('SERVICE_ROLE_KEY', 'default-service-role-key')}
"""
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
                timeout=60
            )

            if result.returncode != 0:
                print(f"Failed to start containers: {result.stderr}")
                raise Exception(f"Docker compose failed: {result.stderr}")

            print(f"Successfully provisioned project {project_id} on ports: DB={db_port}, REST={rest_port}")

        except subprocess.TimeoutExpired:
            raise Exception("Docker compose startup timed out")
        except Exception as e:
            # Clean up on failure
            try:
                subprocess.run(["docker", "compose", "down"], cwd=project_dir, capture_output=True)
            except:
                pass
            raise e

        return {
            "api_url": f"http://localhost:{rest_port}",
            "db_url": f"postgresql://app:{db_password}@localhost:{db_port}/app",
            "realtime_url": f"ws://localhost:{realtime_port}"
        }

    def stop_project(self, project_id: str) -> None:
        # TODO: Implement stop functionality
        pass

    def start_project(self, project_id: str) -> None:
        # TODO: Implement start functionality
        pass

    def delete_project(self, project_id: str) -> None:
        # TODO: Implement delete functionality
        pass

    def restore_project(self, project_id: str) -> None:
        # TODO: Implement restore functionality
        pass
