import sys
import os

# Ensure api/src directory is in python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../api/src'))

from core.database import SessionLocal, engine, Base
from models.plan import Plan, ClusterStrategy
from models.organization_entitlement import OrganizationEntitlement
from models.cluster import Cluster, ClusterType, ClusterStatus
from models.cluster_usage import ClusterUsage
from models.organization import Organization
from models.project import Project
from models.subscription import Subscription

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_plans(db):
    logger.info("Seeding plans...")
    
    plans = [
        {
            "id": "free",
            "name": "Free",
            "monthly_price": 0,
            "max_projects": 2,
            "max_private_clusters": 0,
            "cluster_strategy": ClusterStrategy.global_only,
            "allow_shared_fallback": True,
            "max_db_size_mb": 500,
            "max_storage_mb": 1024,
            "rate_limit_rps": 20
        },
        {
            "id": "pro",
            "name": "Pro",
            "monthly_price": 2500, # $25
            "max_projects": 20,
            "max_private_clusters": 0,
            "cluster_strategy": ClusterStrategy.global_only,
            "allow_shared_fallback": True,
            "max_db_size_mb": 5000,
            "max_storage_mb": 51200,
            "rate_limit_rps": 200
        },
        {
            "id": "premium",
            "name": "Premium",
            "monthly_price": 10000, # $100
            "max_projects": 100,
            "max_private_clusters": 1,
            "cluster_strategy": ClusterStrategy.private_per_org,
            "allow_shared_fallback": True, # Critical adjustment
            "max_db_size_mb": 20000,
            "max_storage_mb": 512000,
            "rate_limit_rps": 1000
        }
    ]

    for plan_data in plans:
        plan = db.query(Plan).filter(Plan.id == plan_data["id"]).first()
        if not plan:
            plan = Plan(**plan_data)
            db.add(plan)
        else:
            # Update existing plan definitions
            for key, value in plan_data.items():
                setattr(plan, key, value)
    
    db.commit()
    logger.info("Plans seeded.")

def migrate_entitlements(db):
    logger.info("Migrating organization entitlements...")
    orgs = db.query(Organization).all()
    
    for org in orgs:
        ent = db.query(OrganizationEntitlement).filter(OrganizationEntitlement.org_id == org.id).first()
        if not ent:
            # Infer plan from deprecated column or default to free
            # Note: Since we removed the column from the model definition, 
            # we might need to query it via raw SQL if the column still exists in DB but not Model.
            # However, assuming we are doing this before dropping the column.
            # But we updated the model file already.
            # Let's default to 'free' for safety, or check subscription.
            
            plan_id = "free"
            if org.subscription and org.subscription.plan_id:
                plan_id = org.subscription.plan_id
            
            ent = OrganizationEntitlement(
                org_id=org.id,
                plan_id=plan_id
            )
            db.add(ent)
            
            # Recalculate usage
            project_count = db.query(Project).filter(Project.org_id == org.id).count()
            ent.projects_used = project_count
            
    db.commit()
    logger.info("Entitlements migrated.")

def apply_schema_changes(db):
    logger.info("Applying schema changes...")
    from sqlalchemy import text
    
    # 1. Add cluster_id to projects
    try:
        db.execute(text("ALTER TABLE projects ADD COLUMN IF NOT EXISTS cluster_id VARCHAR NULL REFERENCES clusters(id)"))
        logger.info("Added cluster_id to projects")
    except Exception as e:
        logger.warning(f"Could not add cluster_id to projects: {e}")
        db.rollback()

    # 2. Add placement to projects
    try:
        db.execute(text("ALTER TABLE projects ADD COLUMN IF NOT EXISTS placement VARCHAR DEFAULT 'shared'"))
        logger.info("Added placement to projects")
    except Exception as e:
        logger.warning(f"Could not add placement to projects: {e}")
        db.rollback()
        
    # 3. Add billing_email to organizations
    try:
        db.execute(text("ALTER TABLE organizations ADD COLUMN IF NOT EXISTS billing_email VARCHAR NULL"))
        logger.info("Added billing_email to organizations")
    except Exception as e:
        logger.warning(f"Could not add billing_email to organizations: {e}")
        db.rollback()
        
    db.commit()

def seed_global_cluster(db):
    logger.info("Seeding global cluster...")
    from services.cluster_service import ClusterService
    ClusterService.get_or_create_global_cluster(db)
    logger.info("Global cluster seeded.")

def main():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        seed_plans(db)
        seed_global_cluster(db)
        
        # Apply schema changes to existing tables BEFORE migrating entitlements
        apply_schema_changes(db)
        
        migrate_entitlements(db)
        
        # We don't drop tables here automatically to prevent data loss.
        # ResourceQuota table can be dropped manually or via Alembic later.
        
    finally:
        db.close()

if __name__ == "__main__":
    main()
