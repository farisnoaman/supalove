from fastapi import APIRouter, HTTPException, Body, Depends
from typing import Dict, Any
from services.secrets_service import get_secrets, set_secret, delete_secret
from api.v1.utils import verify_project_access
from api.v1.deps import get_db, get_current_user
from sqlalchemy.orm import Session
from models.user import User

router = APIRouter(
    prefix="/{project_id}/secrets",
    tags=["secrets"]
)

@router.get("")
def list_secrets(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    return get_secrets(project_id)

@router.post("")
def update_secret(
    project_id: str,
    payload: Dict[str, str] = Body(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    # Payload is expected to be { "key": "MY_KEY", "value": "my_value" }
    # Or simplified { "MY_KEY": "my_value" } - let's support singular update for now via explicit body
    
    key = payload.get("key")
    value = payload.get("value")
    
    if not key:
        raise HTTPException(status_code=400, detail="Key is required")
        
    return set_secret(project_id, key, value)

@router.delete("/{key}")
def remove_secret(
    project_id: str,
    key: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    return delete_secret(project_id, key)
