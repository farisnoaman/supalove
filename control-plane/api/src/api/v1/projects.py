import io
from fastapi import APIRouter, HTTPException, File, UploadFile
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
from services.database_service import DatabaseService
from services.auth_service import AuthService
from services.storage_service import StorageService
from services.backup_service import BackupService

router = APIRouter()
auth_service = AuthService()
storage_service = StorageService()
backup_service = BackupService()

class SQLQuery(BaseModel):
    sql: str

class ProjectCreate(BaseModel):
    custom_domain: str = None

@router.get("/projects")
def list_projects():
    return get_projects()

@router.get("/projects/{project_id}")
def get_project(project_id: str):
    project = get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/projects")
def create(project: ProjectCreate = None):
    custom_domain = project.custom_domain if project else None
    return create_project(custom_domain=custom_domain)

@router.post("/projects/{project_id}/stop")
def stop(project_id: str):
    project = stop_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "stopped", "project_id": project.id}

@router.post("/projects/{project_id}/start")
def start(project_id: str):
    project = start_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "running", "project_id": project.id}

@router.post("/projects/{project_id}/restore")
def restore(project_id: str):
    try:
        project = restore_project(project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return {"status": "stopped", "project_id": project.id}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archived project not found")
    except FileExistsError:
        raise HTTPException(status_code=400, detail="Project is already active")


@router.delete("/projects/{project_id}")
def delete(project_id: str):
    project = delete_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "deleted", "project_id": project.id}

# Database Management Endpoints

@router.get("/projects/{project_id}/tables")
def list_tables(project_id: str):
    """List all tables in the project database"""
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_tables()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/projects/{project_id}/sql")
def execute_sql(project_id: str, query: SQLQuery):
    """Execute SQL query on project database"""
    try:
        db_service = DatabaseService(project_id)
        result = db_service.execute_query(query.sql)
        if result.get("error"):
            return {"success": False, **result}
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/projects/{project_id}/tables/{table_name}/schema")
def get_table_schema(project_id: str, table_name: str):
    """Get schema for a specific table"""
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_table_schema(table_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/projects/{project_id}/tables/{table_name}/data")
def get_table_data(project_id: str, table_name: str, limit: int = 50):
    """Get sample data from a table"""
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_table_data(table_name, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Auth Management Endpoints

class UserCreate(BaseModel):
    email: str
    password: str = None

@router.get("/projects/{project_id}/auth/users")
def list_auth_users(project_id: str):
    print(f"[API] Listing users for project {project_id}")
    try:
        users = auth_service.list_users(project_id)
        print(f"[API] Found {len(users)} users")
        return users
    except Exception as e:
        print(f"[API] Error listing users: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/projects/{project_id}/auth/users")
def create_auth_user(project_id: str, user: UserCreate):
    try:
        return auth_service.create_user(project_id, user.email, user.password)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/projects/{project_id}/auth/users/{user_id}")
def delete_auth_user(project_id: str, user_id: str):
    try:
        auth_service.delete_user(project_id, user_id)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Storage Management Endpoints

@router.get("/projects/{project_id}/storage/buckets")
def list_storage_buckets(project_id: str):
    print(f"[API] Listing buckets for project {project_id}")
    try:
        buckets = storage_service.list_buckets(project_id)
        print(f"[API] Found {len(buckets)} buckets: {buckets}")
        return buckets
    except Exception as e:
        print(f"[API] Error listing buckets: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/projects/{project_id}/storage/buckets/{bucket_name}/objects")
def list_storage_objects(project_id: str, bucket_name: str, prefix: str = None):
    try:
        return storage_service.list_objects(project_id, bucket_name, prefix)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/projects/{project_id}/storage/buckets/{bucket_name}/objects")
async def upload_storage_object(project_id: str, bucket_name: str, file: UploadFile = File(...)):
    print(f"[API] Uploading object to bucket {bucket_name} for project {project_id}")
    try:
        # Read file content
        content = await file.read()
        storage_service.upload_object(
            project_id=project_id,
            bucket_name=bucket_name,
            object_name=file.filename,
            data=io.BytesIO(content),
            length=len(content),
            content_type=file.content_type
        )
        return {"name": file.filename, "size": len(content)}
    except Exception as e:
        print(f"[API] Error uploading object: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/projects/{project_id}/storage/buckets/{bucket_name}/objects/{object_name:path}")
def delete_storage_object(project_id: str, bucket_name: str, object_name: str):
    try:
        storage_service.delete_object(project_id, bucket_name, object_name)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Backup Management Endpoints

@router.post("/projects/{project_id}/backups")
def create_backup(project_id: str):
    """Trigger a manual backup for database and storage"""
    try:
        db_backup = backup_service.backup_database(project_id)
        backup_service.backup_storage(project_id)
        return {"status": "success", "db_backup": db_backup}
    except Exception as e:
        print(f"[API] Backup failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/projects/{project_id}/backups")
def list_backups(project_id: str):
    try:
        return backup_service.list_backups(project_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
