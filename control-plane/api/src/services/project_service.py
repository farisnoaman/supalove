import uuid
from sqlalchemy.orm import Session

from core.database import SessionLocal  # Keeping it if referenced elsewhere or remove if totally unused
from models.project import Project, ProjectStatus, ProjectPlan, BackendType
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
from services.shared_provisioning_service import provision_shared_project



def get_projects(db: Session, org_id: str = None):
    query = db.query(Project).filter(Project.status != ProjectStatus.DELETED)
    if org_id:
        query = query.filter(Project.org_id == org_id)
    return query.all()


def get_project_by_id(db: Session, project_id: str):
    return db.query(Project).filter(Project.id == project_id).first()



def create_project(db: Session, custom_domain: str = None, name: str = None, org_id: str = None, plan: str = "shared"):
    """
    Create a new project with the specified plan.
    
    Args:
        db: Database session
        custom_domain: Optional custom domain for the project
        name: Project name
        org_id: Organization ID
        plan: Either "shared" (default) or "dedicated"
    """
    project_id = uuid.uuid4().hex[:12]
    
    # Determine plan and backend type
    project_plan = ProjectPlan.SHARED if plan == "shared" else ProjectPlan.DEDICATED
    backend_type = BackendType.SHARED_CLUSTER if plan == "shared" else BackendType.LOCAL_DOCKER
    db_name = f"project_{project_id}" if plan == "shared" else None

    try:
        # 1️⃣ Create project in 'CREATING' state
        project = Project(
            id=project_id,
            name=name,
            org_id=org_id,
            status=ProjectStatus.CREATING,
            plan=project_plan,
            backend_type=backend_type,
            db_name=db_name,
        )
        db.add(project)
        db.commit()

        # Update to 'PROVISIONING'
        project.status = ProjectStatus.PROVISIONING
        db.commit()

        # 2️⃣ Generate base secrets
        secrets = generate_project_secrets(db, project_id)

        if custom_domain:
            secrets["CUSTOM_DOMAIN"] = custom_domain

        db.commit()

        # 3️⃣ Branch based on plan
        if project_plan == ProjectPlan.SHARED:
            # Shared plan: Create database in shared cluster, no containers
            provision_output = provision_shared_project(db, project, secrets)
        else:
            # Dedicated plan: Full Docker stack provisioning
            provision_output = provision_project(project_id, secrets, custom_domain=custom_domain)

        # 4️⃣ Mark running
        project.status = ProjectStatus.RUNNING
        db.commit()
        db.refresh(project)

        return {
            "id": project_id,
            "status": project.status,
            "plan": project.plan.value,
            "api_url": provision_output.get("api_url"),
            "db_url": provision_output.get("db_url"),
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

    # Shared projects don't have containers to stop
    if project.plan == ProjectPlan.DEDICATED:
        provision_stop(project_id)
    
    project.status = ProjectStatus.STOPPED
    db.commit()
    db.refresh(project)
    return project


def start_project(db: Session, project_id: str):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    # Shared projects don't have containers to start
    if project.plan == ProjectPlan.DEDICATED:
        provision_start(project_id)
    
    project.status = ProjectStatus.RUNNING
    db.commit()
    db.refresh(project)
    return project


def delete_project(db: Session, project_id: str):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    project.status = ProjectStatus.DELETING
    db.commit()

    # Only destroy containers for dedicated projects
    if project.plan == ProjectPlan.DEDICATED:
        provision_delete(project_id)
    else:
        # For shared projects, drop the database from the shared cluster
        from services.shared_provisioning_service import delete_shared_project
        delete_shared_project(project)
    
    project.status = ProjectStatus.DELETED
    db.commit()
    db.refresh(project)
    return project


def restore_project(db: Session, project_id: str):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    # Only restore containers for dedicated projects
    if project.plan == ProjectPlan.DEDICATED:
        provision_restore(project_id)
    
    # Restored projects are essentially stopped until started explicitly
    project.status = ProjectStatus.STOPPED
    db.commit()
    db.refresh(project)
    return project


