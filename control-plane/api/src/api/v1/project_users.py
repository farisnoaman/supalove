"""
Project Users API

Endpoints for managing users within individual projects.
Supports CRUD operations on project-level users.
"""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from api.v1.deps import get_db, get_current_user
from api.v1.utils import verify_project_access
from models.user import User
from models.project_secret import ProjectSecret
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


# ============================================
# REQUEST/RESPONSE MODELS
# ============================================

class UserCreate(BaseModel):
    email: str
    password: str
    role: str = "member"
    user_metadata: Optional[dict] = None

class UserUpdate(BaseModel):
    role: Optional[str] = None
    user_metadata: Optional[dict] = None

class UserResponse(BaseModel):
    id: str
    email: str
    role: str
    created_at: str
    email_confirmed_at: Optional[str] = None
    user_metadata: dict
    
    class Config:
        from_attributes = True


# ============================================
# ENDPOINTS
# ============================================

@router.get("/{project_id}/users", response_model=List[UserResponse])
def list_project_users(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    List all users in a project.
    
    Returns users from the project's auth.users table.
    """
    verify_project_access(project_id, db, current_user)
    
    try:
        from services.database_service import DatabaseService
        
        db_service = DatabaseService(project_id)
        
        result = db_service.execute_query("""
            SELECT 
                id::text,
                email,
                COALESCE(
                    (user_metadata->>'role')::text,
                    'member'
                ) as role,
                created_at::text,
                email_confirmed_at::text,
                COALESCE(user_metadata, '{}'::jsonb) as user_metadata
            FROM auth.users
            ORDER BY created_at DESC
        """)
        
        if result.get("error"):
            raise HTTPException(status_code=500, detail=result["error"])
        
        return result["rows"]
        
    except Exception as e:
        logger.error(f"Error listing users for project {project_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/{project_id}/users", response_model=UserResponse)
def create_project_user(
    project_id: str,
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a new user in the project.
    
    Creates the user via the shared auth service.
    """
    verify_project_access(project_id, db, current_user)
    
    try:
        from services.project_user_service import ProjectUserService
        
        user_service = ProjectUserService()
        
        result = user_service.create_user(
            project_id=project_id,
            email=user.email,
            password=user.password,
            role=user.role,
            user_metadata=user.user_metadata
        )
        
        # Extract user from response
        if "user" in result:
            user_data = result["user"]
            # Ensure role is in user_data
            if "role" not in user_data:
                user_data["role"] = user.role
            return user_data
        else:
            raise HTTPException(
                status_code=500,
                detail="User created but response format unexpected"
            )
        
    except Exception as e:
        logger.error(f"Error creating user in project {project_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{project_id}/users/{user_id}")
def delete_project_user(
    project_id: str,
    user_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete a user from the project.
    
    Removes the user from the project's auth.users table.
    """
    verify_project_access(project_id, db, current_user)
    
    try:
        from services.database_service import DatabaseService
        
        db_service = DatabaseService(project_id)
        
        # First check if user exists
        check_result = db_service.execute_query(
            f"SELECT id FROM auth.users WHERE id = '{user_id}'"
        )
        
        if check_result.get("error") or not check_result.get("rows"):
            raise HTTPException(status_code=404, detail="User not found")
        
        # Delete user
        result = db_service.execute_query(
            f"DELETE FROM auth.users WHERE id = '{user_id}'"
        )
        
        if result.get("error"):
            raise HTTPException(status_code=500, detail=result["error"])
        
        return {
            "status": "deleted",
            "user_id": user_id,
            "message": "User deleted successfully"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting user {user_id} from project {project_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{project_id}/admin-password")
def get_admin_temp_password(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get the temporary admin password (one-time retrieval).
    
    This password is generated when the project is created and can
    only be retrieved once. After retrieval, it is deleted.
    """
    verify_project_access(project_id, db, current_user)
    
    try:
        secret = db.query(ProjectSecret).filter(
            ProjectSecret.project_id == project_id,
            ProjectSecret.key == "ADMIN_TEMP_PASSWORD"
        ).first()
        
        if not secret:
            raise HTTPException(
                status_code=404,
                detail="Admin password not found or already retrieved"
            )
        
        # Get password and delete (one-time use)
        password = secret.value
        db.delete(secret)
        db.commit()
        
        logger.info(f"Admin password retrieved for project {project_id}")
        
        return {
            "password": password,
            "message": "This password will not be shown again. Please save it securely."
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving admin password for project {project_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
