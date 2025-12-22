from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from services.project_service import (
    create_project,
    get_projects,
    get_project_by_id,
    stop_project,
    start_project,
    delete_project,
    restore_project,
)
from api.v1.deps import get_current_user, get_db
from models.user import User
from models.org_member import OrgMember, OrgRole
from sqlalchemy.orm import Session
from api.v1.utils import verify_project_access
from models.project import Project
from models.resource_quota import ResourceQuota

router = APIRouter()

class ProjectCreate(BaseModel):
    custom_domain: str = None
    name: str = None
    org_id: str = None

@router.get("")
def list_projects(
    org_id: str = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if org_id:
        # Verify user belongs to this org
        member_record = db.query(OrgMember).filter(
            OrgMember.user_id == current_user.id, 
            OrgMember.org_id == org_id
        ).first()
        if not member_record:
            raise HTTPException(status_code=403, detail="Not authorized for this organization")
        
        return get_projects(db, org_id=org_id)
    
    # Fallback to primary org if no org_id specified (backward compatibility)
    member_record = db.query(OrgMember).filter(OrgMember.user_id == current_user.id).first()
    if not member_record:
        return []

    return get_projects(db, org_id=member_record.org_id)

@router.get("/{project_id}")
def get_project(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    project = get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("")
def create(
    project: ProjectCreate = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    target_org_id = None
    if project and project.org_id:
        # Verify access to provided org
        member_record = db.query(OrgMember).filter(
            OrgMember.user_id == current_user.id,
            OrgMember.org_id == project.org_id
        ).first()
        if not member_record:
             raise HTTPException(status_code=403, detail="Not authorized for this organization")
        target_org_id = project.org_id
    else:
        # Fallback to primary org
        member_record = db.query(OrgMember).filter(OrgMember.user_id == current_user.id).first()
        if not member_record:
            raise HTTPException(status_code=400, detail="User does not belong to an organization")
        target_org_id = member_record.org_id

    # Check quotas
    quota = db.query(ResourceQuota).filter(ResourceQuota.org_id == target_org_id).first()
    # Default quotas if not defined: 3 projects
    max_projects = quota.max_projects if quota else 3
    
    current_count = db.query(Project).filter(Project.org_id == target_org_id).count()
    if current_count >= max_projects:
        raise HTTPException(status_code=400, detail=f"Project quota reached ({max_projects})")

    custom_domain = project.custom_domain if project else None
    name = project.name if project else None

    # Pass org_id to service
    return create_project(db, custom_domain=custom_domain, name=name, org_id=target_org_id)

@router.post("/{project_id}/stop")
def stop(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    project = stop_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "stopped", "project_id": project.id}

@router.post("/{project_id}/start")
def start(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    project = start_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "running", "project_id": project.id}

@router.post("/{project_id}/restore")
def restore(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    try:
        project = restore_project(db, project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return {"status": "stopped", "project_id": project.id}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archived project not found")
    except FileExistsError:
        raise HTTPException(status_code=400, detail="Project is already active")

@router.delete("/{project_id}")
def delete(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    project = delete_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "deleted", "project_id": project.id}


@router.get("/{project_id}/config")
def get_project_config(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    
    # Fetch secrets
    from models.project_secret import ProjectSecret
    secrets = db.query(ProjectSecret).filter(ProjectSecret.project_id == project_id).all()
    secrets_map = {s.key: s.value for s in secrets}
    
    if not secrets_map:
         raise HTTPException(status_code=404, detail="Project configuration not found")

    # Construct keys
    # We need to generate JWTs on the fly using the project's JWT_SECRET
    jwt_secret = secrets_map.get("JWT_SECRET")
    if not jwt_secret:
         raise HTTPException(status_code=500, detail="Project JWT secret is missing")
    
    from jose import jwt
    import datetime
    
    # Helper to generate permanent tokens (or long lived)
    def generate_token(role: str, secret: str):
        payload = {
            "role": role,
            "iss": "supalove",
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=365*10) # 10 years
        }
        return jwt.encode(payload, secret, algorithm="HS256")

    anon_key = generate_token("anon", jwt_secret)
    service_role_key = generate_token("service_role", jwt_secret)
    
    # Construct URLs
    # Assuming localhost for now as per plan, but respecting ports
    rest_port = secrets_map.get("REST_PORT", "3000")
    db_port = secrets_map.get("DB_PORT", "5432")
    db_pass = secrets_map.get("DB_PASSWORD", "postgres")
    auth_port = secrets_map.get("AUTH_PORT", "9999")
    realtime_port = secrets_map.get("REALTIME_PORT", "4000")
    storage_port = secrets_map.get("STORAGE_PORT", "5000")
    functions_port = secrets_map.get("FUNCTIONS_PORT", "8000")
    
    # Use stored keys if available, otherwise generate on the fly
    anon_key = secrets_map.get("ANON_KEY") or generate_token("anon", jwt_secret)
    service_role_key = secrets_map.get("SERVICE_ROLE_KEY") or generate_token("service_role", jwt_secret)
    
    # Masked DB URL for display
    db_url = f"postgresql://postgres:[YOUR-PASSWORD]@localhost:{db_port}/postgres"
    
    return {
        # API URLs
        "api_url": f"http://localhost:{rest_port}",
        "auth_url": f"http://localhost:{auth_port}",
        "realtime_url": f"ws://localhost:{realtime_port}",
        "storage_url": f"http://localhost:{storage_port}",
        "functions_url": f"http://localhost:{functions_port}",
        # Database
        "db_url": db_url,
        "db_host": "localhost",
        "db_port": db_port,
        "db_user": "postgres",
        "db_pass": db_pass,
        # Keys
        "anon_key": anon_key,
        "service_role_key": service_role_key,
        "jwt_secret": jwt_secret
    }


# ============================================
# DEPLOYMENT ENDPOINTS
# ============================================

import os

@router.get("/{project_id}/deployment")
def get_deployment_config(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get deployment configuration and status for a project."""
    verify_project_access(project_id, db, current_user)
    
    # Check if Coolify is configured
    coolify_url = os.getenv("COOLIFY_API_URL")
    coolify_token = os.getenv("COOLIFY_API_TOKEN")
    coolify_connected = bool(coolify_url and coolify_token)
    
    # Determine environment
    environment = "coolify" if coolify_connected else "local"
    
    # Get custom domain from secrets
    from models.project_secret import ProjectSecret
    domain_secret = db.query(ProjectSecret).filter(
        ProjectSecret.project_id == project_id,
        ProjectSecret.key == "CUSTOM_DOMAIN"
    ).first()
    
    return {
        "environment": environment,
        "coolify_connected": coolify_connected,
        "custom_domain": domain_secret.value if domain_secret else None,
        "ssl_enabled": coolify_connected and domain_secret is not None,
        "deployment_url": f"https://{domain_secret.value}" if domain_secret else None
    }


class DomainConfig(BaseModel):
    domain: str


@router.post("/{project_id}/deployment/domain")
def set_custom_domain(
    project_id: str,
    config: DomainConfig,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Set a custom domain for the project."""
    verify_project_access(project_id, db, current_user)
    
    from models.project_secret import ProjectSecret
    
    # Upsert the custom domain
    existing = db.query(ProjectSecret).filter(
        ProjectSecret.project_id == project_id,
        ProjectSecret.key == "CUSTOM_DOMAIN"
    ).first()
    
    if existing:
        existing.value = config.domain
    else:
        db.add(ProjectSecret(
            project_id=project_id,
            key="CUSTOM_DOMAIN",
            value=config.domain
        ))
    
    db.commit()
    
    return {"status": "saved", "domain": config.domain}


@router.post("/{project_id}/deployment/redeploy")
def redeploy_project(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Trigger a redeployment of the project (Coolify only)."""
    verify_project_access(project_id, db, current_user)
    
    coolify_url = os.getenv("COOLIFY_API_URL")
    coolify_token = os.getenv("COOLIFY_API_TOKEN")
    
    if not coolify_url or not coolify_token:
        raise HTTPException(status_code=400, detail="Coolify not configured")
    
    from services.provisioning_coolify import CoolifyProvisioner
    
    provisioner = CoolifyProvisioner(coolify_url, coolify_token)
    resource = provisioner._find_resource_by_name(f"project-{project_id}")
    
    if not resource:
        raise HTTPException(status_code=404, detail="Project not found in Coolify")
    
    # Trigger deploy
    provisioner._make_request("POST", f"/api/v1/applications/{resource['uuid']}/deploy")
    
    return {"status": "deploying"}

