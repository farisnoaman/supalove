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
    verify_project_access(project_id, db, current_user)
    try:
        return backup_service.list_backups(project_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
