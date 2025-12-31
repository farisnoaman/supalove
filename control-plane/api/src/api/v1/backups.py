from fastapi import APIRouter, HTTPException, Depends
from services.backup_service import BackupService
from api.v1.utils import verify_project_access
from api.v1.deps import get_db, get_current_user
from sqlalchemy.orm import Session
from models.user import User

router = APIRouter()
backup_service = BackupService()

@router.post("/{project_id}/backups")
def create_backup(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Trigger a manual backup for database and storage"""
    verify_project_access(project_id, db, current_user)
    try:
        db_backup = backup_service.backup_database(project_id)
        backup_service.backup_storage(project_id)
        return {"status": "success", "db_backup": db_backup}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}/backups")
def list_backups(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all backups for a project"""
    verify_project_access(project_id, db, current_user)
    try:
        return backup_service.list_backups(project_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}/backups/{backup_id:path}/download")
def download_backup(
    project_id: str,
    backup_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a download URL for a backup"""
    verify_project_access(project_id, db, current_user)
    try:
        # backup_id comes URL-encoded, decode the path
        from urllib.parse import unquote
        backup_path = unquote(backup_id)
        return backup_service.download_backup(project_id, backup_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/backups/{backup_id:path}/restore")
def restore_backup(
    project_id: str,
    backup_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Restore a backup (WARNING: This will overwrite current data!)"""
    verify_project_access(project_id, db, current_user)
    try:
        from urllib.parse import unquote
        backup_path = unquote(backup_id)
        return backup_service.restore_backup(project_id, backup_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
