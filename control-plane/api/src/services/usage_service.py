from sqlalchemy.orm import Session
from models.organization import Organization
from models.project import Project
from models.usage_record import UsageRecord
from fastapi import HTTPException

print(f"DEBUG: Loading usage_service from {__file__}")

class UsageService:
    def __init__(self, db: Session):
        self.db = db

    def get_current_usage(self, org_id: str) -> dict:
        """
        Calculates real-time usage for an organization.
        """
        # 1. Project Count
        project_count = self.db.query(Project).filter_by(org_id=org_id).count()

        # 2. Database Size (Mock for now, would use pg_database_size)
        # In a real scenario, we'd query the stats DB or cache this value.
        db_size_mb = project_count * 50 # Assume 50MB per project for now

        # 3. Storage Size (Mock for now, would query MinIO)
        storage_size_mb = project_count * 100 # Assume 100MB per project

        return {
            "projects": project_count,
            "db_size_mb": db_size_mb,
            "storage_mb": storage_size_mb
        }

    def check_limit(self, org_id: str, resource_type: str, increment: int = 1) -> bool:
        """
        Checks if adding 'increment' to 'resource_type' would exceed the quota.
        resource_type: 'projects', 'db_size_mb', 'storage_mb'
        """
        from services.entitlement_service import EntitlementService
        
        if resource_type == "projects":
            # Use the canonical entitlement check
            try:
                # This throws HTTP 403 if failed, so we catch or just use boolean logic if we had it
                # check_can_create_project raises exception.
                # Let's see EntitlementService implementation.
                EntitlementService.check_can_create_project(self.db, org_id)
                return True
            except HTTPException:
                return False
            except Exception:
                # If plan allows unlimited (-1), check_can_create_project handles it.
                return False

        # For other resources, manually check against Plan
        ent = EntitlementService.get_entitlements(self.db, org_id)
        plan = EntitlementService.get_plan(self.db, ent.plan_id)
        usage = self.get_current_usage(org_id)
        
        if resource_type == "db_size_mb":
            if plan.max_db_size_mb == -1: return True
            return (usage["db_size_mb"] + (increment * 50)) <= plan.max_db_size_mb
            
        elif resource_type == "storage_mb":
            if plan.max_storage_mb == -1: return True
            return (usage["storage_mb"] + (increment * 100)) <= plan.max_storage_mb

        return True

    def get_usage_summary(self, org_id: str) -> dict:
        """
        Returns usage vs limits for UI.
        """
        from services.entitlement_service import EntitlementService
        
        usage = self.get_current_usage(org_id)
        ent = EntitlementService.get_entitlements(self.db, org_id)
        plan = EntitlementService.get_plan(self.db, ent.plan_id)
        
        limit_projects = plan.max_projects
        limit_db = plan.max_db_size_mb
        limit_storage = plan.max_storage_mb

        return {
            "projects": {
                "used": usage["projects"],
                "limit": limit_projects,
                "percent": 0 if limit_projects == -1 else min(100, int((usage["projects"] / limit_projects) * 100))
            },
            "db_size": {
                "used_mb": usage["db_size_mb"],
                "limit_mb": limit_db,
                "percent": 0 if limit_db == -1 else min(100, int((usage["db_size_mb"] / limit_db) * 100))
            },
            "storage": {
                "used_mb": usage["storage_mb"],
                "limit_mb": limit_storage,
                "percent": 0 if limit_storage == -1 else min(100, int((usage["storage_mb"] / limit_storage) * 100))
            }
        }
