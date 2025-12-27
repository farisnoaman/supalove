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
        from models.project import Project, ProjectStatus
        
        ent = EntitlementService.get_entitlements(db, org_id)
        plan = EntitlementService.get_plan(db, ent.plan_id)
        
        if plan.max_projects == -1:  # Unlimited
            return True
            
        # Dynamic Count (Source of Truth)
        current_count = db.query(Project).filter(
            Project.org_id == org_id,
            Project.status != ProjectStatus.DELETED
        ).count()
        
        if current_count >= plan.max_projects:
            raise HTTPException(
                status_code=403,
                detail=f"Project limit reached ({plan.max_projects}). Upgrade your plan."
            )
        
        return True
    
    @staticmethod
    def increment_project_count(db: Session, org_id: str):
        """Deprecated: Counters are unreliable. Use dynamic counts."""
        pass
    
    @staticmethod
    def decrement_project_count(db: Session, org_id: str):
        """Deprecated: Counters are unreliable. Use dynamic counts."""
        pass
