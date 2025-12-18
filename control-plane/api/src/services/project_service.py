import uuid
from sqlalchemy.orm import Session

from core.database import SessionLocal
from models.project import Project
from services.secrets_service import generate_project_secrets
from services.provisioning_service import provision_project


def create_project():
    project_id = uuid.uuid4().hex[:12]
    db: Session = SessionLocal()

    # 1️⃣ Create project
    project = Project(id=project_id, status="provisioning")
    db.add(project)
    db.commit()

    # 2️⃣ Generate secrets (RETURN them)
    secrets = generate_project_secrets(db, project_id)

    # 3️⃣ Provision infra using secrets
    provision_project(project_id, secrets)

    # 4️⃣ Mark running
    project.status = "running"
    db.commit()

    return {
        "project_id": project_id,
        "status": project.status,
        "api_url": f"http://localhost:{project_id}"
    }
