from fastapi import APIRouter, HTTPException, Query, Depends
from services.logs_service import get_project_logs
from api.v1.utils import verify_project_access
from api.v1.deps import get_db, get_current_user
from sqlalchemy.orm import Session
from models.user import User

router = APIRouter(
    prefix="/{project_id}/logs",
    tags=["logs"]
)

@router.get("")
def fetch_logs(
    project_id: str, 
    service: str = Query(..., description="Service name (database, auth, api, storage, realtime)"),
    lines: int = Query(100, ge=1, le=2000),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = verify_project_access(project_id, db, current_user)
    from models.project import ProjectPlan
    is_shared = project.plan == ProjectPlan.shared
    logs = get_project_logs(project_id, service, lines, is_shared=is_shared)
    return {"logs": logs}
