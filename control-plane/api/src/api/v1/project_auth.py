"""
Project Auth API Endpoints

Manages per-project user authentication via GoTrue proxy.
Falls back to control-plane database if GoTrue is not available.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
import asyncio

from api.v1.deps import get_db, get_current_user
from models.user import User as PlatformUser
from api.v1.utils import verify_project_access
from services.gotrue_proxy_service import GoTrueProxyService

router = APIRouter()


class ProjectUserCreate(BaseModel):
    email: str
    password: str
    username: Optional[str] = None


class ProjectUserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    user_metadata: Optional[dict] = None


class ProjectUserResponse(BaseModel):
    id: str
    email: str
    username: Optional[str] = None
    enabled: bool
    createdTimestamp: int

    class Config:
        orm_mode = True


@router.get("", response_model=List[ProjectUserResponse])
def list_users(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: PlatformUser = Depends(get_current_user)
):
    """List all users in the project's GoTrue instance."""
    verify_project_access(project_id, db, current_user)
    
    gotrue = GoTrueProxyService(db, project_id)
    
    # Run async method in sync context
    try:
        users = asyncio.get_event_loop().run_until_complete(gotrue.list_users())
    except RuntimeError:
        # If no event loop, create one
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        users = loop.run_until_complete(gotrue.list_users())
    
    return users


@router.post("", response_model=ProjectUserResponse)
def create_user(
    project_id: str,
    user_in: ProjectUserCreate,
    db: Session = Depends(get_db),
    current_user: PlatformUser = Depends(get_current_user)
):
    """Create a new user in the project's GoTrue instance."""
    verify_project_access(project_id, db, current_user)
    
    gotrue = GoTrueProxyService(db, project_id)
    
    user_metadata = None
    if user_in.username:
        user_metadata = {"username": user_in.username}
    
    # Run async method in sync context
    try:
        user = asyncio.get_event_loop().run_until_complete(
            gotrue.create_user(user_in.email, user_in.password, user_metadata)
        )
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        user = loop.run_until_complete(
            gotrue.create_user(user_in.email, user_in.password, user_metadata)
        )
    
    if not user:
        raise HTTPException(
            status_code=500, 
            detail="Failed to create user. GoTrue may not be running or user already exists."
        )
    
    return user


@router.get("/{user_id}", response_model=ProjectUserResponse)
def get_user(
    project_id: str,
    user_id: str,
    db: Session = Depends(get_db),
    current_user: PlatformUser = Depends(get_current_user)
):
    """Get a specific user from the project's GoTrue instance."""
    verify_project_access(project_id, db, current_user)
    
    gotrue = GoTrueProxyService(db, project_id)
    
    try:
        user = asyncio.get_event_loop().run_until_complete(gotrue.get_user(user_id))
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        user = loop.run_until_complete(gotrue.get_user(user_id))
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user


@router.put("/{user_id}", response_model=ProjectUserResponse)
def update_user(
    project_id: str,
    user_id: str,
    user_update: ProjectUserUpdate,
    db: Session = Depends(get_db),
    current_user: PlatformUser = Depends(get_current_user)
):
    """Update a user in the project's GoTrue instance."""
    verify_project_access(project_id, db, current_user)
    
    gotrue = GoTrueProxyService(db, project_id)
    
    update_data = {}
    if user_update.email:
        update_data["email"] = user_update.email
    if user_update.password:
        update_data["password"] = user_update.password
    if user_update.user_metadata:
        update_data["user_metadata"] = user_update.user_metadata
    
    try:
        user = asyncio.get_event_loop().run_until_complete(
            gotrue.update_user(user_id, update_data)
        )
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        user = loop.run_until_complete(gotrue.update_user(user_id, update_data))
    
    if not user:
        raise HTTPException(status_code=500, detail="Failed to update user")
    
    return user


@router.delete("/{user_id}")
def delete_user(
    project_id: str,
    user_id: str,
    db: Session = Depends(get_db),
    current_user: PlatformUser = Depends(get_current_user)
):
    """Delete a user from the project's GoTrue instance."""
    verify_project_access(project_id, db, current_user)
    
    gotrue = GoTrueProxyService(db, project_id)
    
    try:
        success = asyncio.get_event_loop().run_until_complete(gotrue.delete_user(user_id))
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        success = loop.run_until_complete(gotrue.delete_user(user_id))
    
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete user")
    
    return {"status": "deleted", "id": user_id}


@router.get("/health")
def auth_health(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: PlatformUser = Depends(get_current_user)
):
    """Check if GoTrue is healthy for this project."""
    verify_project_access(project_id, db, current_user)
    
    gotrue = GoTrueProxyService(db, project_id)
    
    try:
        healthy = asyncio.get_event_loop().run_until_complete(gotrue.check_health())
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        healthy = loop.run_until_complete(gotrue.check_health())
    
    return {
        "healthy": healthy,
        "auth_url": gotrue.auth_url
    }
