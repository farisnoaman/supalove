from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.auth_service import AuthService
from api.v1.utils import validate_project_access

router = APIRouter()
auth_service = AuthService()

class UserCreate(BaseModel):
    email: str
    password: str = None

@router.get("/{project_id}/auth/users")
def list_auth_users(project_id: str):
    validate_project_access(project_id)
    try:
        return auth_service.list_users(project_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/auth/users")
def create_auth_user(project_id: str, user: UserCreate):
    validate_project_access(project_id)
    try:
        return auth_service.create_user(project_id, user.email, user.password)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{project_id}/auth/users/{user_id}")
def delete_auth_user(project_id: str, user_id: str):
    validate_project_access(project_id)
    try:
        auth_service.delete_user(project_id, user_id)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
