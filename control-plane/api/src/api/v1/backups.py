from fastapi import APIRouter, HTTPException
from services.backup_service import BackupService
from api.v1.utils import validate_project_access

router = APIRouter()
backup_service = BackupService()

@router.post("/{project_id}/backups")
def create_backup(project_id: str):
    """Trigger a manual backup for database and storage"""
    validate_project_access(project_id)
    try:
        db_backup = backup_service.backup_database(project_id)
        backup_service.backup_storage(project_id)
        return {"status": "success", "db_backup": db_backup}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}/backups")
def list_backups(project_id: str):
    validate_project_access(project_id)
    try:
        return backup_service.list_backups(project_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
