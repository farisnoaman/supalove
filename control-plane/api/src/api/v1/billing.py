from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from pydantic import BaseModel
from api.v1.deps import get_current_user, get_db
from models.user import User
from models.org_member import OrgMember, OrgRole
from models.subscription import Subscription
from services.billing_service import BillingService
import os

router = APIRouter()
billing_service = BillingService()

class CheckoutRequest(BaseModel):
    plan_id: str
    return_url: str

class PortalRequest(BaseModel):
    return_url: str

@router.post("/orgs/{org_id}/checkout")
def create_checkout_session(
    org_id: str,
    req: CheckoutRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verify access (owner only)
    member = db.query(OrgMember).filter(
        OrgMember.org_id == org_id,
        OrgMember.user_id == current_user.id,
        OrgMember.role == OrgRole.OWNER
    ).first()
    
    if not member:
        raise HTTPException(status_code=403, detail="Only owners can manage billing")

    session_url = billing_service.create_checkout_session(
        org_id=org_id,
        plan_id=req.plan_id,
        success_url=f"{req.return_url}?success=true",
        cancel_url=f"{req.return_url}?canceled=true"
    )
    
    # If mock, simulate success immediately for dev experience
    if "mock.stripe.com" in session_url:
        return {"url": session_url, "mock": True}
        
    return {"url": session_url}

@router.post("/orgs/{org_id}/portal")
def create_portal_session(
    org_id: str,
    req: PortalRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verify access
    member = db.query(OrgMember).filter(
        OrgMember.org_id == org_id,
        OrgMember.user_id == current_user.id,
        OrgMember.role == OrgRole.OWNER
    ).first()
    
    if not member:
        raise HTTPException(status_code=403, detail="Only owners can manage billing")
        
    sub = db.query(Subscription).filter(Subscription.org_id == org_id).first()
    if not sub or not sub.stripe_customer_id:
        raise HTTPException(status_code=400, detail="No billing account found")
        
    url = billing_service.create_portal_session(sub.stripe_customer_id, req.return_url)
    return {"url": url}

@router.get("/orgs/{org_id}/subscription")
def get_subscription(
    org_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    member = db.query(OrgMember).filter(
        OrgMember.org_id == org_id,
        OrgMember.user_id == current_user.id
    ).first()
    
    if not member:
        raise HTTPException(status_code=403, detail="Not authorized")
        
    sub = db.query(Subscription).filter(Subscription.org_id == org_id).first()
    
    return {
        "status": sub.status if sub else "free",
        "plan": sub.plan_id if sub else "free",
        "current_period_end": sub.current_period_end if sub else None
    }

@router.get("/orgs/{org_id}/usage")
def get_usage(
    org_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    member = db.query(OrgMember).filter(
        OrgMember.org_id == org_id,
        OrgMember.user_id == current_user.id
    ).first()
    
    if not member:
        raise HTTPException(status_code=403, detail="Not authorized")
        
    from services.usage_service import UsageService
    usage_service = UsageService(db)
    
    return usage_service.get_usage_summary(org_id)

@router.post("/webhook")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    
    return billing_service.handle_webhook(payload, sig_header, db)


# ============================================
# DEV-ONLY UPGRADE ENDPOINT (No Stripe)
# ============================================

class DevUpgradeRequest(BaseModel):
    plan_id: str  # "free", "pro", "premium"

@router.post("/orgs/{org_id}/dev-upgrade")
def dev_upgrade_plan(
    org_id: str,
    req: DevUpgradeRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    DEV ONLY: Directly upgrade an organization's plan without going through Stripe.
    This endpoint should be disabled in production.
    """
    # Verify access (owner only)
    member = db.query(OrgMember).filter(
        OrgMember.org_id == org_id,
        OrgMember.user_id == current_user.id,
        OrgMember.role == OrgRole.OWNER
    ).first()
    
    if not member:
        raise HTTPException(status_code=403, detail="Only owners can manage billing")
        
    # Validate plan exists
    from models.plan import Plan
    plan_exists = db.query(Plan).filter(Plan.id == req.plan_id).first()
    if not plan_exists:
        raise HTTPException(status_code=400, detail=f"Plan '{req.plan_id}' does not exist")
    
    # Update or create subscription
    sub = db.query(Subscription).filter(Subscription.org_id == org_id).first()
    if not sub:
        sub = Subscription(org_id=org_id)
        db.add(sub)
    
    sub.plan_id = req.plan_id
    sub.status = "active" if req.plan_id != "free" else "free"
    sub.stripe_customer_id = f"dev_customer_{org_id[:8]}"
    sub.stripe_subscription_id = f"dev_sub_{org_id[:8]}"
    
    # Update Entitlements
    from services.entitlement_service import EntitlementService
    ent = EntitlementService.get_entitlements(db, org_id)
    ent.plan_id = req.plan_id
    
    db.commit()
    
    return {
        "status": "success",
        "message": f"Organization upgraded to {req.plan_id} plan (DEV MODE)",
        "plan": req.plan_id
    }
