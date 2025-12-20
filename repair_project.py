#scripts/provision_project.py
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
