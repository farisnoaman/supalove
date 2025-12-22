from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
import uuid
import time

from api.v1.deps import get_db, get_current_user
from models.user import User as PlatformUser
from models.project_user import ProjectUser
from api.v1.utils import verify_project_access

router = APIRouter()

class ProjectUserCreate(BaseModel):
    email: str
    password: str
    username: Optional[str] = None

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
    verify_project_access(project_id, db, current_user) # Ensure platform user owns project
    users = db.query(ProjectUser).filter(ProjectUser.project_id == project_id).all()
    return users

@router.post("", response_model=ProjectUserResponse)
def create_user(
    project_id: str,
    user_in: ProjectUserCreate,
    db: Session = Depends(get_db),
    current_user: PlatformUser = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    
    # Check duplicate in this project
    existing = db.query(ProjectUser).filter(
        ProjectUser.project_id == project_id, 
        ProjectUser.email == user_in.email
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists in this project")

    new_user = ProjectUser(
        id=str(uuid.uuid4()),
        project_id=project_id,
        email=user_in.email,
        username=user_in.username or user_in.email,
        enabled=True,
        createdTimestamp=int(time.time() * 1000)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete("/{user_id}")
def delete_user(
    project_id: str,
    user_id: str,
    db: Session = Depends(get_db),
    current_user: PlatformUser = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    user = db.query(ProjectUser).filter(
        ProjectUser.project_id == project_id,
        ProjectUser.id == user_id
    ).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    db.delete(user)
    db.commit()
    return {"status": "deleted", "id": user_id}
