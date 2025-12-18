import os
import sys
from pathlib import Path
from typing import Dict, Any

# Adjust path to find scripts
PROJECT_ROOT = Path(__file__).resolve().parents[4]
sys.path.append(str(PROJECT_ROOT))

from scripts.provision_project import provision_project as script_provision
from scripts.lifecycle import (
    stop_project as script_stop,
    start_project as script_start,
    delete_project as script_delete,
    restore_project as script_restore,
)
from services.provisioning_interface import ProvisioningProvider

BASE_PROJECTS_DIR = PROJECT_ROOT / "data-plane" / "projects"

class LocalProvisioner(ProvisioningProvider):
    """Local Docker Compose based provisioner"""
    
    def provision_project(self, project_id: str, secrets: dict = None) -> Dict[str, Any]:
        """Provisions a new project using local Docker Compose scripts."""
        # If no secrets provided, generate empty dict (script will generate them)
        if secrets is None:
            secrets = {}
            
        env_vars = script_provision(project_id, secrets, BASE_PROJECTS_DIR)
        
        api_port = env_vars["REST_PORT"]
        db_port = env_vars["DB_PORT"]
        realtime_port = env_vars["REALTIME_PORT"]
        
        return {
            "api_url": f"http://localhost:{api_port}",
            "db_url": f"postgresql://app:{env_vars['DB_PASSWORD']}@localhost:{db_port}/app",
            "realtime_url": f"ws://localhost:{realtime_port}"
        }

    def stop_project(self, project_id: str):
        return script_stop(project_id, BASE_PROJECTS_DIR)

    def start_project(self, project_id: str):
        return script_start(project_id, BASE_PROJECTS_DIR)

    def delete_project(self, project_id: str):
        return script_delete(project_id, BASE_PROJECTS_DIR)

    def restore_project(self, project_id: str):
        return script_restore(project_id, BASE_PROJECTS_DIR)
