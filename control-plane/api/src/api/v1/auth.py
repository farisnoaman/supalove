from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from core.database import SessionLocal
from models.user import User
from models.organization import Organization
from models.org_member import OrgMember, OrgRole
from services.auth_service import AuthService
from datetime import timedelta

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Models (DTOs)
class UserCreate(BaseModel):
    email: str
    password: str
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id: str
    email: str
    full_name: Optional[str] = None
    
    class Config:
        orm_mode = True

@router.post("/register", response_model=Token)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # 1. Check if user exists
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. Create User
    hashed_password = AuthService.get_password_hash(user_in.password)
    new_user = User(
        email=user_in.email,
        hashed_password=hashed_password,
        full_name=user_in.full_name
    )
    db.add(new_user)
    db.flush() # get ID

    # 3. Create Default Organization ("Personal")
    org_name = f"{user_in.full_name or 'User'}'s Org"
    # Simple slug generation
    slug_base = user_in.email.split('@')[0]
    org_slug = slug_base
    counter = 1
    while db.query(Organization).filter(Organization.slug == org_slug).first():
        org_slug = f"{slug_base}-{counter}"
        counter += 1

    new_org = Organization(name=org_name, slug=org_slug)
    db.add(new_org)
    db.flush()

    # 4. Add User as Owner of Org
    member = OrgMember(
        user_id=new_user.id,
        org_id=new_org.id,
        role=OrgRole.OWNER
    )
    db.add(member)
    db.commit()

    # 5. Generate Token
    access_token = AuthService.create_access_token(data={"sub": new_user.id})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(login_in: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_in.email).first()
    if not user or not AuthService.verify_password(login_in.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = AuthService.create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

# TODO: Add /me endpoint with authentication dependency
