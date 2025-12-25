from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from api.v1.deps import get_current_user, get_db
from models.user import User
from models.organization import Organization
from models.org_member import OrgMember, OrgRole
import uuid

router = APIRouter()

# DTOs
class OrgCreate(BaseModel):
    name: str
    slug: str

class OrgResponse(BaseModel):
    id: str
    name: str
    slug: str
    plan: str
    role: str = None # User's role in this org

    class Config:
        from_attributes = True

class MemberAdd(BaseModel):
    email: str
    role: OrgRole = OrgRole.MEMBER

class MemberResponse(BaseModel):
    id: str
    user_id: str
    email: str
    role: OrgRole
    full_name: Optional[str] = None

@router.get("", response_model=List[OrgResponse])
def list_organizations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List all organizations the current user receives."""
    memberships = db.query(OrgMember).filter(OrgMember.user_id == current_user.id).all()
    orgs = []
    for m in memberships:
        org = db.query(Organization).filter(Organization.id == m.org_id).first()
        if org:
            # Attach role for the response
            org_dict = org.__dict__
            org_dict['role'] = m.role
            orgs.append(org_dict)
    return orgs

@router.post("", response_model=OrgResponse)
def create_organization(
    org_in: OrgCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new organization."""
    # Check slug uniqueness
    if db.query(Organization).filter(Organization.slug == org_in.slug).first():
        raise HTTPException(status_code=400, detail="Organization slug already exists")

    new_org = Organization(
        name=org_in.name,
        slug=org_in.slug
    )
    db.add(new_org)
    db.flush()

    # Add creator as owner
    member = OrgMember(
        user_id=current_user.id,
        org_id=new_org.id,
        role=OrgRole.OWNER
    )
    db.add(member)
    db.commit()
    db.refresh(new_org)
    
    org_dict = new_org.__dict__
    org_dict['role'] = OrgRole.OWNER
    return org_dict

@router.get("/{org_id}/members", response_model=List[MemberResponse])
def list_members(
    org_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List members of an organization."""
    # Verify access
    user_membership = db.query(OrgMember).filter(
        OrgMember.user_id == current_user.id,
        OrgMember.org_id == org_id
    ).first()
    
    if not user_membership:
        raise HTTPException(status_code=403, detail="Not a member of this organization")

    members = db.query(OrgMember).filter(OrgMember.org_id == org_id).all()
    response = []
    for m in members:
        user = db.query(User).filter(User.id == m.user_id).first()
        if user:
            response.append({
                "id": m.id,
                "user_id": user.id,
                "email": user.email,
                "full_name": user.full_name,
                "role": m.role
            })
    return response

@router.post("/{org_id}/members", response_model=MemberResponse)
def add_member(
    org_id: str,
    member_in: MemberAdd,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Add a member to the organization by email."""
    # Verify access (Only Admins/Owners)
    user_membership = db.query(OrgMember).filter(
        OrgMember.user_id == current_user.id,
        OrgMember.org_id == org_id
    ).first()
    
    if not user_membership or user_membership.role not in [OrgRole.OWNER, OrgRole.ADMIN]:
        raise HTTPException(status_code=403, detail="Only admins can add members")

    # Find user by email
    target_user = db.query(User).filter(User.email == member_in.email).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="User not found (User must allow discovery or register first)")

    # Check if already member
    if db.query(OrgMember).filter(OrgMember.user_id == target_user.id, OrgMember.org_id == org_id).first():
        raise HTTPException(status_code=400, detail="User is already a member")

    new_member = OrgMember(
        user_id=target_user.id,
        org_id=org_id,
        role=member_in.role
    )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)

    return {
        "id": new_member.id,
        "user_id": target_user.id,
        "email": target_user.email,
        "full_name": target_user.full_name,
        "role": new_member.role
    }
