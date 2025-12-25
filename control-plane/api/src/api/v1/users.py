from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
import json

from api.v1.deps import get_db, get_current_user
from models.user import User

router = APIRouter()

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    timezone: Optional[str] = None
    theme: Optional[str] = None

class UserProfile(BaseModel):
    id: str
    email: str
    full_name: Optional[str]
    timezone: str
    avatar_url: Optional[str]
    preferences: Optional[dict]

    class Config:
        from_attributes = True

@router.get("/me", response_model=UserProfile)
def get_me(
    current_user: User = Depends(get_current_user)
):
    # Parse preferences JSON if it exists
    prefs = {}
    if current_user.preferences:
        try:
            prefs = json.loads(current_user.preferences)
        except:
            pass
            
    return UserProfile(
        id=current_user.id,
        email=current_user.email,
        full_name=current_user.full_name,
        timezone=current_user.timezone or "UTC",
        avatar_url=current_user.avatar_url,
        preferences=prefs
    )

@router.patch("/me", response_model=UserProfile)
def update_me(
    user_in: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if user_in.full_name is not None:
        current_user.full_name = user_in.full_name
    
    if user_in.timezone is not None:
        current_user.timezone = user_in.timezone

    # Handle theme preference via preferences JSON
    if user_in.theme:
        prefs = {}
        if current_user.preferences:
            try:
                prefs = json.loads(current_user.preferences)
            except:
                pass
        prefs["theme"] = user_in.theme
        current_user.preferences = json.dumps(prefs)

    db.commit()
    db.refresh(current_user)
    
    # Return formatted
    prefs = {}
    if current_user.preferences:
        try:
            prefs = json.loads(current_user.preferences)
        except:
            pass
            
    return UserProfile(
        id=current_user.id,
        email=current_user.email,
        full_name=current_user.full_name,
        timezone=current_user.timezone or "UTC",
        avatar_url=current_user.avatar_url,
        preferences=prefs
    )
