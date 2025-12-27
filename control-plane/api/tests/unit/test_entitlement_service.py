import pytest
import uuid
from services.entitlement_service import EntitlementService
from models.organization import Organization
from models.user import User

@pytest.fixture
def test_org(db):
    # Setup test user and org
    user = User(id=str(uuid.uuid4()), email=f"svc_test{uuid.uuid4()}@test.com", hashed_password="pw")
    db.add(user)
    db.flush()
    
    org = Organization(id=str(uuid.uuid4()), name="Svc Test Org", slug=f"svc-org-{uuid.uuid4()}")
    db.add(org)
    db.commit()
    
    # Ensure entitlement exists
    # We use EntitlementService.get_entitlements to ensure record creation
    ent = EntitlementService.get_entitlements(db, org.id)
    # Ensure it is free (default)
    if ent.plan_id != "free":
        ent.plan_id = "free"
        db.commit()
    
    return org

def set_test_plan(db, org_id, plan_id):
    entitlement = EntitlementService.get_entitlements(db, org_id)
    entitlement.plan_id = plan_id
    db.commit()

def test_check_can_create_project_under_limit(db, test_org):
    """Test that a user can create a project when under the limit"""
    # Free plan limit is 2
    
    # Case 1: 0 projects used
    assert EntitlementService.check_can_create_project(db, test_org.id) is True

def test_check_can_create_project_over_limit(db, test_org):
    """Test that creating project is blocked when limit reached"""
    # Free plan limit is 2. Manually set used to 2.
    entitlement = EntitlementService.get_entitlements(db, test_org.id)
    entitlement.projects_used = 2
    db.commit()
    
    # Should fail
    # Note: method raises HTTPException, so test for that
    from fastapi import HTTPException
    
    try:
        EntitlementService.check_can_create_project(db, test_org.id)
        assert False, "Should have raised HTTPException"
    except HTTPException as e:
        assert e.status_code == 403

def test_upgrade_plan(db, test_org):
    """Test upgrading plan updates the entitlement"""
    # Upgrade to pro
    set_test_plan(db, test_org.id, "pro")
    
    entitlement = EntitlementService.get_entitlements(db, test_org.id)
    assert entitlement.plan_id == "pro"
    
    # Check limit increases (Pro limit is 20)
    entitlement.projects_used = 5
    db.commit()
    
    # Should be allowed now (5 < 20)
    assert EntitlementService.check_can_create_project(db, test_org.id) is True
