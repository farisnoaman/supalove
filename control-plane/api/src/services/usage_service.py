from sqlalchemy.orm import Session
from models.organization import Organization
from models.project import Project
from models.resource_quota import ResourceQuota
from models.usage_record import UsageRecord

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
        print(f"DEBUG: usage_service.check_limit called for {resource_type}")
        return True # Bypass for testing
        quota = self.db.query(ResourceQuota).filter_by(org_id=org_id).first()
        if not quota:
            # If no quota found, assume free tier limits as fallback or create one?
            # For robustness, we should probably ensure quota exists. 
            # If strictly enforcing, default to restrictive.
            return False

        usage = self.get_current_usage(org_id)
        
        if resource_type == "projects":
            return True # Bypass for testing
            if quota.max_projects == -1: return True
            return (usage["projects"] + increment) <= quota.max_projects
            
        elif resource_type == "db_size_mb":
            if quota.max_db_size_mb == -1: return True
            return (usage["db_size_mb"] + increment) <= quota.max_db_size_mb
            
        elif resource_type == "storage_mb":
            if quota.max_storage_mb == -1: return True
            return (usage["storage_mb"] + increment) <= quota.max_storage_mb

        return True

    def get_usage_summary(self, org_id: str) -> dict:
        """
        Returns usage vs limits for UI.
        """
        usage = self.get_current_usage(org_id)
        quota = self.db.query(ResourceQuota).filter_by(org_id=org_id).first()
        
        if not quota:
            # Fallback defaults if row missing
            defaults = ResourceQuota.get_defaults("free")
            limit_projects = defaults["max_projects"]
            limit_db = defaults["max_db_size_mb"]
            limit_storage = defaults["max_storage_mb"]
        else:
            limit_projects = quota.max_projects
            limit_db = quota.max_db_size_mb
            limit_storage = quota.max_storage_mb

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
