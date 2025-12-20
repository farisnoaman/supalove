Step 5: Replace Shell Scripts with Coolify API
Goal Description
Transition from local Docker Compose scripts to a proper orchestration API using Coolify. To ensure robustness and easier testing, we will first refactor the current provisioning logic into a modular ProvisioningProvider interface. This allows us to support both "Local Docker" (legacy/dev) and "Coolify" (prod) backends.

User Review Required
IMPORTANT

Configuration Required: To use Coolify, you must provide COOLIFY_API_URL and COOLIFY_API_TOKEN in your 
.env
. If not provided, the system will default to the existing Local Docker provisioner.

NOTE

This plan introduces a Strategy Pattern for provisioning.

Proposed Changes
1. Refactoring: Provisioning Interface
[NEW] 
provisioning_interface.py
Define abstract base class ProvisioningProvider with methods:
provision_project(project_id: str) -> dict
stop_project(project_id: str)
start_project(project_id: str)
delete_project(project_id: str)
restore_project(project_id: str)
2. Implementation: Local Provider
[NEW] 
provisioning_local.py
Moves logic from 
provisioning_service.py
 functions into LocalProvisioner class.
Calls existing 
scripts/provision_project.py
 and 
scripts/lifecycle.py
.
3. Implementation: Coolify Provider
[NEW] 
provisioning_coolify.py
Implements CoolifyProvisioner.
Uses httpx to communicate with Coolify API (v4).
Maps operations:
provision_project
 -> Create Project/Resource in Coolify.
stop/start/delete -> Call respective Coolify endpoints.
4. Service Layer Update
[MODIFY] 
provisioning_service.py
Delete old procedural functions.
Instantiate the correct provider based on env vars:
if os.getenv("COOLIFY_API_URL"):
    provider = CoolifyProvisioner(...)
else:
    provider = LocalProvisioner(...)
Expose methods that delegate to provider.
Verification Plan
1. Regression Test (Local)
Ensure COOLIFY_API_URL is unset.
Run POST /projects.
Verify docker ps shows containers (Local Docker).
2. Coolify Test (Mock/Real)
Set COOLIFY_API_URL=https://demo.coolify.io/api/v1 (or mock).
Run POST /projects.
Verify code attempts to call Coolify API (check logs).

-----
## repair_project.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys
from pathlib import Path

# Setup paths
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(PROJECT_ROOT / "control-plane" / "api" / "src"))

from core.database import DATABASE_URL
from models.project import Project
from models.project_secret import ProjectSecret
from services.provisioning_service import provision_project

def repair_project(project_id):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    db = Session()

    try:
        # Get project
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            print(f"Project {project_id} not found")
            return

        # Get secrets
        secrets_rows = db.query(ProjectSecret).filter(ProjectSecret.project_id == project_id).all()
        secrets = {row.key: row.value for row in secrets_rows}

        if not secrets:
            print(f"No secrets found for project {project_id}")
            return

        print(f"Repairing project {project_id}...")
        print(f"Using secrets: {list(secrets.keys())}")

        # Re-provision
        provision_project(project_id, secrets)
        
        print(f"Project {project_id} repaired and started successfully.")

    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python repair_project.py <project_id>")
    else:
        repair_project(sys.argv[1])

---------
