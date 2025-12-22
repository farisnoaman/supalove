import uuid
from sqlalchemy.orm import Session

from core.database import SessionLocal  # Keeping it if referenced elsewhere or remove if totally unused
from models.project import Project, ProjectStatus
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



def get_projects(db: Session, org_id: str = None):
    query = db.query(Project).filter(Project.status != ProjectStatus.DELETED)
    if org_id:
        query = query.filter(Project.org_id == org_id)
    return query.all()


def get_project_by_id(db: Session, project_id: str):
    return db.query(Project).filter(Project.id == project_id).first()



def create_project(db: Session, custom_domain: str = None, name: str = None, org_id: str = None):
    project_id = uuid.uuid4().hex[:12]

    try:
        # 1️⃣ Create project in 'CREATING' state
        project = Project(
            id=project_id,
            name=name,
            org_id=org_id,
            status=ProjectStatus.CREATING
        )
        db.add(project)
        db.commit()

        # Update to 'PROVISIONING'
        project.status = ProjectStatus.PROVISIONING
        db.commit()

        # 2️⃣ Generate base secrets
        secrets = generate_project_secrets(db, project_id)

        # 3️⃣ Auth Setup (Keycloak)
        # auth_service = AuthService()
        # realm_name = auth_service.create_project_realm(project_id)
        # auth_config = auth_service.create_api_client(realm_name)
        
        # Store auth secrets
        # from models.project_secret import ProjectSecret
        # db.add(ProjectSecret(project_id=project_id, key="AUTH_REALM", value=realm_name))
        # db.add(ProjectSecret(project_id=project_id, key="AUTH_CLIENT_ID", value=auth_config["client_id"]))
        # db.add(ProjectSecret(project_id=project_id, key="AUTH_CLIENT_SECRET", value=auth_config["client_secret"]))
        
        # secrets.update({
        #     "AUTH_REALM": realm_name,
        #     "AUTH_CLIENT_ID": auth_config["client_id"],
        #     "AUTH_CLIENT_SECRET": auth_config["client_secret"]
        # })

        # 4️⃣ Storage Setup (MinIO)
        # storage_service = StorageService()
        # bucket_name = storage_service.create_project_bucket(project_id)
        # storage_config = storage_service.get_storage_config(bucket_name)
        
        # Store storage secrets
        # for key, value in storage_config.items():
        #     db.add(ProjectSecret(project_id=project_id, key=key, value=value))
        
        # secrets.update(storage_config)
        
        if custom_domain:
            # db.add(ProjectSecret(project_id=project_id, key="CUSTOM_DOMAIN", value=custom_domain))
            secrets["CUSTOM_DOMAIN"] = custom_domain

        db.commit()

        # 5️⃣ Provision infra using consolidated secrets
        provision_output = provision_project(project_id, secrets, custom_domain=custom_domain)

        # 6️⃣ Mark running
        project.status = ProjectStatus.RUNNING
        db.commit()
        db.refresh(project)

        return {
            "project_id": project_id,
            "status": project.status,
            "api_url": provision_output["api_url"],
            "db_url": provision_output["db_url"],
        }
    except Exception as e:
        db.rollback()
        # Mark as failed and store error
        failed_project = db.query(Project).filter(Project.id == project_id).first()
        if failed_project:
            failed_project.status = ProjectStatus.FAILED
            failed_project.last_error = str(e)
            db.commit()
        raise e



def stop_project(db: Session, project_id: str):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    project.status = ProjectStatus.STOPPED
    provision_stop(project_id)
    db.commit()
    db.refresh(project)
    return project


def start_project(db: Session, project_id: str):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    project.status = ProjectStatus.RUNNING
    provision_start(project_id)
    db.commit()
    db.refresh(project)
    return project


def delete_project(db: Session, project_id: str):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    project.status = ProjectStatus.DELETING
    db.commit()

    provision_delete(project_id)
    
    project.status = ProjectStatus.DELETED
    db.commit()
    db.refresh(project)
    return project


def restore_project(db: Session, project_id: str):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    provision_restore(project_id)
    # Restored projects are essentially stopped until started explicitly
    project.status = ProjectStatus.STOPPED
    db.commit()
    db.refresh(project)
    return project

