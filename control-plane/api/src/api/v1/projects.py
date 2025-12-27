from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
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

router = APIRouter()

class ProjectCreate(BaseModel):
    custom_domain: str = None
    name: str = None
    org_id: str = None
    plan: str = "shared"  # "shared" or "dedicated"

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
    from services.usage_service import UsageService
    usage_service = UsageService(db)
    
    if not usage_service.check_limit(target_org_id, "projects"):
        raise HTTPException(status_code=402, detail="Project limit reached. Please upgrade your plan.")

    custom_domain = project.custom_domain if project else None
    name = project.name if project else None
    plan = project.plan if project else "shared"

    # Pass org_id and plan to service
    return create_project(db, custom_domain=custom_domain, name=name, org_id=target_org_id, plan=plan)

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

@router.post("/{project_id}/import")
def import_backup(
    project_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Import a Supabase backup (.pg or .gz)"""
    verify_project_access(project_id, db, current_user)
    
    import shutil
    import subprocess
    from pathlib import Path
    import logging

    logger = logging.getLogger(__name__)

    # Security check: Ensure file extension is valid
    if not (file.filename.endswith(".pg") or file.filename.endswith(".gz") or file.filename.endswith(".sql")):
         raise HTTPException(status_code=400, detail="Invalid file type. Allowed: .pg, .gz, .sql")

    # Save uploaded file
    tmp_path = Path(f"/tmp/{file.filename}")
    try:
        logger.info(f"Starting import for project {project_id} with file {file.filename}")
        
        with tmp_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        logger.info(f"File saved to {tmp_path}, size: {tmp_path.stat().st_size} bytes")
            
        # Delegate to the robust import script
        script_path = Path("/home/faris/Documents/MyApps/supalove/scripts/import_backup.py")
        
        if not script_path.exists():
            logger.error(f"Import script not found at {script_path}")
            raise HTTPException(status_code=500, detail=f"Import script not found at {script_path}")
        
        # We need to run this as a subprocess
        # python3 scripts/import_backup.py <PROJECT_ID> <FILE_PATH>
        cmd = ["python3", str(script_path), project_id, str(tmp_path)]
        logger.info(f"Executing command: {' '.join(cmd)}")
        
        process = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        # Log the output for debugging
        logger.info(f"Import script stdout: {process.stdout}")
        if process.stderr:
            logger.warning(f"Import script stderr: {process.stderr}")
        
        if process.returncode != 0:
            error_msg = f"Import script failed with exit code {process.returncode}"
            logger.error(f"{error_msg}\nStderr: {process.stderr}\nStdout: {process.stdout}")
            
            # Provide more specific error details
            details = []
            if process.stderr:
                details.append(f"Error output: {process.stderr[:500]}")
            if process.stdout:
                details.append(f"Script output: {process.stdout[:500]}")
            
            return {
                "status": "error", 
                "message": f"Import failed: {error_msg}", 
                "details": details
            }
        
        logger.info(f"Import completed successfully for project {project_id}")
        return {"status": "success", "message": "Backup imported successfully", "details": [process.stdout[-200:] if process.stdout else ""]}

    except subprocess.TimeoutExpired:
        logger.error(f"Import script timed out for project {project_id}")
        raise HTTPException(status_code=500, detail="Import operation timed out (max 5 minutes)")
    except Exception as e:
        logger.exception(f"Import failed for project {project_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Import failed: {str(e)}")
    finally:
        # Cleanup local tmp file
        if tmp_path.exists():
            tmp_path.unlink()
            logger.info(f"Cleaned up temporary file {tmp_path}")

@router.post("/{project_id}/import-from-migrations")
def import_from_migrations(
    project_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Import from Supabase migration-based backup (for inactive/deleted projects)"""
    verify_project_access(project_id, db, current_user)
    
    import shutil
    import subprocess
    from pathlib import Path
    import logging
    import re

    logger = logging.getLogger(__name__)

    # Security check
    if not (file.filename.endswith(".pg") or file.filename.endswith(".gz") or file.filename.endswith(".sql")):
         raise HTTPException(status_code=400, detail="Invalid file type. Allowed: .pg, .gz, .sql")

    # Save uploaded file
    tmp_path = Path(f"/tmp/{file.filename}")
    try:
        logger.info(f"Starting migration extraction for project {project_id} with file {file.filename}")
        
        with tmp_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        logger.info(f"File saved to {tmp_path}, size: {tmp_path.stat().st_size} bytes")
            
        # Use migration extraction script
        script_path = Path("/home/faris/Documents/MyApps/supalove/scripts/extract_from_migrations.py")
        
        if not script_path.exists():
            logger.error(f"Migration extraction script not found at {script_path}")
            raise HTTPException(status_code=500, detail=f"Migration extraction script not found at {script_path}")
        
        cmd = ["python3", str(script_path), project_id, str(tmp_path)]
        logger.info(f"Executing command: {' '.join(cmd)}")
        
        process = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        # Log the output for debugging
        logger.info(f"Migration extraction stdout: {process.stdout}")
        if process.stderr:
            logger.warning(f"Migration extraction stderr: {process.stderr}")
        
        if process.returncode != 0:
            error_msg = f"Migration extraction script failed with exit code {process.returncode}"
            logger.error(f"{error_msg}\nStderr: {process.stderr}\nStdout: {process.stdout}")
            
            # Check if no migrations were found (common case)
            if "No migration data found" in process.stdout:
                return {
                    "status": "error",
                    "message": "No migration data found in backup file. This backup might be a standard SQL dump. Try using the 'Import Database Backup' option instead.",
                    "details": [process.stdout[:500]]
                }
            
            # Provide detailed error information
            details = []
            if process.stderr:
                details.append(f"Error output: {process.stderr[:500]}")
            if process.stdout:
                details.append(f"Script output: {process.stdout[:500]}")
            
            return {
                "status": "error", 
                "message": f"Migration extraction failed: {error_msg}", 
                "details": details
            }
        
        # Count how many migrations were extracted
        migrations_count = len(re.findall(r'✓ Found migration', process.stdout))
        logger.info(f"Successfully extracted {migrations_count} migrations for project {project_id}")
        
        return {
            "status": "success", 
            "message": f"Successfully extracted and executed {migrations_count} migrations",
            "details": [process.stdout[-300:] if process.stdout else ""]
        }

    except subprocess.TimeoutExpired:
        logger.error(f"Migration extraction timed out for project {project_id}")
        raise HTTPException(status_code=500, detail="Migration extraction operation timed out (max 5 minutes)")
    except Exception as e:
        logger.exception(f"Migration extraction failed for project {project_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Migration extraction failed: {str(e)}")
    finally:
        # Cleanup local tmp file
        if tmp_path.exists():
            tmp_path.unlink()
            logger.info(f"Cleaned up temporary file {tmp_path}")

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
    print(f"DEBUG: Project {project_id} secrets: {list(secrets_map.keys())}")
    
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
    gateway_port = secrets_map.get("GATEWAY_PORT")
    
    if gateway_port:
        base_url = f"http://localhost:{gateway_port}"
        api_url = f"{base_url}/rest/v1"
        auth_url = f"{base_url}/auth/v1"
        realtime_url = f"ws://localhost:{gateway_port}/realtime/v1"
        storage_url = f"{base_url}/storage/v1"
        functions_url = f"{base_url}/functions/v1"
    else:
        # Fallback for old projects without gateway
        api_url = f"http://localhost:{rest_port}"
        auth_url = f"http://localhost:{auth_port}"
        realtime_url = f"ws://localhost:{realtime_port}"
        storage_url = f"http://localhost:{storage_port}"
        functions_url = f"http://localhost:{functions_port}"

    # Masked DB URL for display
    db_url = f"postgresql://postgres:[YOUR-PASSWORD]@localhost:{db_port}/postgres"

    return {
        # API URLs
        "api_url": base_url if gateway_port else api_url, # For Supabase Client, this is the main URL
        # Specific service endpoints (useful for debugging or internal routing if needed)
        "rest_url": api_url,
        "auth_url": auth_url,
        "realtime_url": realtime_url,
        "storage_url": storage_url,
        "functions_url": functions_url,
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

