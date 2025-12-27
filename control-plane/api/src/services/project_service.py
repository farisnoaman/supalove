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
        plan: Explicit placement "shared" or "private" (was 'dedicated') or None to infer
    """
    # 1️⃣ Check Entitlements
    from services.entitlement_service import EntitlementService
    EntitlementService.check_can_create_project(db, org_id)

    # 2️⃣ Resolve Cluster
    from services.cluster_service import ClusterService
    from models.cluster import ClusterStatus
    
    # Determine explicit placement if provided
    placement = None
    if plan == "private":
        placement = "private"
    elif plan == "shared":
        placement = "shared"
        
    cluster = ClusterService.resolve_cluster_for_project(db, org_id)
    
    project_id = uuid.uuid4().hex[:12]
    
    # Determine plan and backend type based on cluster
    # Note: 'dedicated' in ProjectPlan is now essentially 'running in private cluster' or 'dedicated-single'
    # For now, we map private_shared cluster projects to essentially look like 'shared' backend type 
    # but routed to a different URL.
    
    # However, to keep compatible with "Private Shared" architecture:
    # Projects in private shared cluster share the cluster resources but have own DBs.
    
    project_status = ProjectStatus.CREATING
    
    # If using Global Cluster -> BackendType.shared_cluster
    # If using Private Cluster -> BackendType.shared_cluster (but different host)
    
    backend_type = BackendType.shared_cluster
    db_name = f"project_{project_id}"

    try:
        # 3️⃣ Create project record
        project = Project(
            id=project_id,
            name=name,
            org_id=org_id,
            cluster_id=cluster.id,
            status=project_status,
            plan=ProjectPlan.shared, # All projects are 'shared' resource usage wise (db only), unless dedicated_single
            backend_type=backend_type,
            db_name=db_name,
            placement=placement
        )
        db.add(project)
        db.commit()

        # 4️⃣ Generate secrets
        secrets = generate_project_secrets(db, project_id, plan="shared")
        if custom_domain:
            secrets["CUSTOM_DOMAIN"] = custom_domain
        db.commit()

        # 5️⃣ Provisioning Logic
        # If cluster is creating, we MUST wait (Async)
        if cluster.status == ClusterStatus.creating:
            # Leave as CREATING. Scheduler will pick up Cluster provisioning.
            # We also need a way for Project to transition to RUNNING once Cluster is ready.
            # For now, let's assume Scheduler also checks "Creating" projects in "Running" clusters?
            # Or simpler: The API returns creating, FE polls. 
            pass
        
        elif cluster.status == ClusterStatus.running:
            # Cluster ready, provision immediately
            project.status = ProjectStatus.PROVISIONING
            db.commit()
            
            # Provision project DB in the resolved cluster
            provision_output = provision_shared_project(db, project, cluster, secrets)
            
            project.status = ProjectStatus.RUNNING
            EntitlementService.increment_project_count(db, org_id)
            db.commit()
            db.refresh(project)
            
            return {
                "id": project_id,
                "status": project.status,
                "plan": project.plan.value,
                "api_url": provision_output.get("api_url"),
                "db_url": provision_output.get("db_url"),
            }

        return {
            "id": project_id,
            "status": project.status,
            "plan": project.plan.value,
            "api_url": None, # Not ready
            "db_url": None,
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
    if project.plan == ProjectPlan.dedicated:
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
    if project.plan == ProjectPlan.dedicated:
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
    if project.plan == ProjectPlan.dedicated:
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
    if project.plan == ProjectPlan.dedicated:
        provision_restore(project_id)
    
    # Restored projects are essentially stopped until started explicitly
    project.status = ProjectStatus.STOPPED
    db.commit()
    db.refresh(project)
    return project


