from fastapi import APIRouter, HTTPException, Query
from services.logs_service import get_project_logs
from api.v1.utils import validate_project_access

router = APIRouter(
    prefix="/{project_id}/logs",
    tags=["logs"]
)

@router.get("")
def fetch_logs(
    project_id: str, 
    service: str = Query(..., description="Service name (database, auth, api, storage, realtime)"),
    lines: int = Query(100, ge=1, le=2000)
):
    validate_project_access(project_id)
    logs = get_project_logs(project_id, service, lines)
    return {"logs": logs}
