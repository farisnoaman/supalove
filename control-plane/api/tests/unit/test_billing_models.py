import pytest
from sqlalchemy.exc import IntegrityError
from models.plan import Plan, ClusterStrategy
from models.organization import Organization
from models.organization_entitlement import OrganizationEntitlement
from models.user import User
import uuid

def test_create_plans(db):
    """Test creating plans works correctly"""
    # Create a new test plan
    plan_id = f"test_plan_{uuid.uuid4()}"
    plan = Plan(
        id=plan_id,
        name="Test Plan",
        monthly_price=1000,
        max_projects=5,
        max_db_size_mb=1000,
        max_storage_mb=10000,
        cluster_strategy=ClusterStrategy.global_only,
        allow_shared_fallback=True
    )
    db.add(plan)
    db.commit()

    # Retrieve it
    fetched = db.query(Plan).filter(Plan.id == plan_id).first()
    assert fetched is not None
    assert fetched.name == "Test Plan"
    assert fetched.cluster_strategy == ClusterStrategy.global_only

def test_organization_entitlement_relationship(db):
    """Test the one-to-one relationship between Org and Entitlement"""
    # Create Org (User required first usually, but Org logic might vary. 
    # Assuming Org requires owner_id, so let's create a User first to be safe, 
    # though strict FK might not be enforced in sqlite if used, but here uses pg)
    
    # Create dummy user
    user = User(id=str(uuid.uuid4()), email=f"test{uuid.uuid4()}@test.com", hashed_password="pw")
    db.add(user)
    db.flush()

    # Create Org (owner_id is not a column on Organization, handled via OrgMember)
    org = Organization(id=str(uuid.uuid4()), name="Test Org", slug=f"test-org-{uuid.uuid4()}")
    db.add(org)
    db.commit()

    # Check default entitlement (if hook exists) or create one
    # Assuming our migration/business logic creates it, but here we test model directly
    
    entitlement = OrganizationEntitlement(
        org_id=org.id,
        plan_id="free", # Assuming 'free' exists from seed or we just use a string
        projects_used=0
    )
    db.add(entitlement)
    db.commit()

    # Refresh org
    db.refresh(org)
    
    # Assert relationship
    assert org.entitlement is not None
    assert org.entitlement.plan_id == "free"
    assert org.entitlement.org_id == org.id
