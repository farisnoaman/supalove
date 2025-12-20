import uuid
from sqlalchemy.orm import Session

from core.database import SessionLocal
from models.project import Project
from services.secrets_service import generate_project_secrets
from services.auth_service import AuthService
from services.storage_service import StorageService
from services.provisioning_service import (
    provision_project,
    stop_project as provision_stop,
    start_project as provision_start,
    delete_project as provision_delete,
    restore_project as provision_restore,
)


def get_projects():
    db: Session = SessionLocal()
    return db.query(Project).all()


def get_project_by_id(project_id: str):
    db: Session = SessionLocal()
    return db.query(Project).filter(Project.id == project_id).first()


def create_project(custom_domain: str = None):
    project_id = uuid.uuid4().hex[:12]
    db: Session = SessionLocal()

    # 1️⃣ Create project
    project = Project(id=project_id, status="provisioning")
    db.add(project)
    db.commit()

    # 2️⃣ Generate base secrets
    secrets = generate_project_secrets(db, project_id)

    # 3️⃣ Auth Setup (Keycloak)
    auth_service = AuthService()
    realm_name = auth_service.create_project_realm(project_id)
    auth_config = auth_service.create_api_client(realm_name)
    
    # Store auth secrets
    from models.project_secret import ProjectSecret
    db.add(ProjectSecret(project_id=project_id, key="AUTH_REALM", value=realm_name))
    db.add(ProjectSecret(project_id=project_id, key="AUTH_CLIENT_ID", value=auth_config["client_id"]))
    db.add(ProjectSecret(project_id=project_id, key="AUTH_CLIENT_SECRET", value=auth_config["client_secret"]))
    
    secrets.update({
        "AUTH_REALM": realm_name,
        "AUTH_CLIENT_ID": auth_config["client_id"],
        "AUTH_CLIENT_SECRET": auth_config["client_secret"]
    })

    # 4️⃣ Storage Setup (MinIO)
    storage_service = StorageService()
    bucket_name = storage_service.create_project_bucket(project_id)
    storage_config = storage_service.get_storage_config(bucket_name)
    
    # Store storage secrets
    for key, value in storage_config.items():
        db.add(ProjectSecret(project_id=project_id, key=key, value=value))
    
    secrets.update(storage_config)
    

    if custom_domain:
        db.add(ProjectSecret(project_id=project_id, key="CUSTOM_DOMAIN", value=custom_domain))
        secrets["CUSTOM_DOMAIN"] = custom_domain

    db.commit()

    # 5️⃣ Provision infra using consolidated secrets
    provision_output = provision_project(project_id, secrets, custom_domain=custom_domain)

    # 6️⃣ Mark running
    db.query(Project).filter(Project.id == project_id).update({"status": "running"})
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
    db.query(Project).filter(Project.id == project_id).update({"status": "stopped"})
    db.commit()
    db.refresh(project)
    return project


def start_project(project_id: str):
    db: Session = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    provision_start(project_id)
    db.query(Project).filter(Project.id == project_id).update({"status": "running"})
    db.commit()
    db.refresh(project)
    return project


def delete_project(project_id: str):
    db: Session = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    provision_delete(project_id)
    db.query(Project).filter(Project.id == project_id).update({"status": "deleted"})
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
    db.query(Project).filter(Project.id == project_id).update({"status": "stopped"})
    db.commit()
    db.refresh(project)
    return project
