from sqlalchemy.orm import Session
from models.organization_entitlement import OrganizationEntitlement
from models.plan import Plan, ClusterStrategy
from fastapi import HTTPException

class EntitlementService:
    @staticmethod
    def get_entitlements(db: Session, org_id: str) -> OrganizationEntitlement:
        """Get current entitlements for an organization."""
        ent = db.query(OrganizationEntitlement).filter(
            OrganizationEntitlement.org_id == org_id
        ).first()
        
        if not ent:
            # Default to free plan
            ent = OrganizationEntitlement(org_id=org_id, plan_id="free")
            db.add(ent)
            db.commit()
        
        return ent
    
    @staticmethod
    def get_plan(db: Session, plan_id: str) -> Plan:
        """Get plan details."""
        return db.query(Plan).filter(Plan.id == plan_id).first()
    
    @staticmethod
    def check_can_create_project(db: Session, org_id: str) -> bool:
        """Check if org can create another project."""
        ent = EntitlementService.get_entitlements(db, org_id)
        plan = EntitlementService.get_plan(db, ent.plan_id)
        
        if plan.max_projects == -1:  # Unlimited
            return True
        
        if ent.projects_used >= plan.max_projects:
            raise HTTPException(
                status_code=403,
                detail=f"Project limit reached ({plan.max_projects}). Upgrade your plan."
            )
        
        return True
    
    @staticmethod
    def increment_project_count(db: Session, org_id: str):
        """Increment project counter."""
        ent = EntitlementService.get_entitlements(db, org_id)
        ent.projects_used += 1
        db.commit()
    
    @staticmethod
    def decrement_project_count(db: Session, org_id: str):
        """Decrement project counter."""
        ent = EntitlementService.get_entitlements(db, org_id)
        if ent.projects_used > 0:
            ent.projects_used -= 1
            db.commit()
