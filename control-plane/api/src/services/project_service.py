import uuid
from sqlalchemy.orm import Session

from core.database import SessionLocal
from models.project import Project
from services.secrets_service import generate_project_secrets
from services.provisioning_service import (
    provision_project,
    stop_project as provision_stop,
    start_project as provision_start,
    delete_project as provision_delete,
    restore_project as provision_restore,
)


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
    provision_output = provision_project(project_id, secrets)

    # 4️⃣ Mark running
    project.status = "running"
    db.commit()
    db.refresh(project)

    return {
        "project_id": project_id,
        "status": project.status,
        "api_url": provision_output["api_url"],
        "db_url": provision_output["db_url"],
    }


def stop_project(project_id: str):
    db: Session = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    provision_stop(project_id)
    project.status = "stopped"
    db.commit()
    db.refresh(project)
    return project


def start_project(project_id: str):
    db: Session = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    provision_start(project_id)
    project.status = "running"
    db.commit()
    db.refresh(project)
    return project


def delete_project(project_id: str):
    db: Session = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    provision_delete(project_id)
    project.status = "deleted" 
    # Soft delete: We keep the row but mark as deleted.
    db.commit()
    db.refresh(project)
    return project


def restore_project(project_id: str):
    db: Session = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    provision_restore(project_id)
    # Restored projects are essentially stopped until started explicitly
    project.status = "stopped"
    db.commit()
    db.refresh(project)
    return project
