import pytest
from models.organization import Organization
from models.user import User
from models.org_member import OrgMember, OrgRole
from models.subscription import Subscription
import uuid

@pytest.fixture
def auth_org(db, auth_headers):
    # We need to find the org that belongs to the test user in auth_headers
    # The 'auth_headers' fixture creates a user "faris1@faris.com" (if not exists)
    # We need to ensure this user has an org for testing
    
    user_email = "faris1@faris.com"
    user = db.query(User).filter(User.email == user_email).first()
    
    # Check if user has an org where they are owner
    member = db.query(OrgMember).filter(OrgMember.user_id == user.id, OrgMember.role == OrgRole.OWNER).first()
    
    if member:
        org = db.query(Organization).filter(Organization.id == member.org_id).first()
        
        # Ensure entitlement
        from services.entitlement_service import EntitlementService
        # No set_plan on service
        
        ent = EntitlementService.get_entitlements(db, org.id)
        if ent.plan_id != "free":
            ent.plan_id = "free"
            db.commit()
            
        subscription = db.query(Subscription).filter(Subscription.org_id == org.id).first()
        if subscription and subscription.plan_id != "free":
            subscription.plan_id = "free"
            subscription.status = "active"
            db.commit()
            
        return org
        
    # Create new org for this user
    org = Organization(id=str(uuid.uuid4()), name="API Test Org", slug=f"api-test-{uuid.uuid4()}")
    db.add(org)
    
    member = OrgMember(org_id=org.id, user_id=user.id, role=OrgRole.OWNER)
    db.add(member)
    db.commit()
    
    # Ensure entitlement (new orgs default to free via get_entitlements side effect if accessed)
    from services.entitlement_service import EntitlementService
    EntitlementService.get_entitlements(db, org.id)
    
    return org

@pytest.mark.asyncio
async def test_get_subscription(client, auth_headers, auth_org):
    """Test GET /subscription endpoint"""
    resp = await client.get(f"/api/v1/billing/orgs/{auth_org.id}/subscription", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["plan"] == "free" # Should default to free

@pytest.mark.asyncio
async def test_dev_upgrade_flow(client, auth_headers, auth_org, db):
    """Test the DEV ONLY upgrade endpoint"""
    # 1. Verify currently free
    resp = await client.get(f"/api/v1/billing/orgs/{auth_org.id}/subscription", headers=auth_headers)
    assert resp.json()["plan"] == "free"

    # 2. Call dev-upgrade to 'pro'
    resp = await client.post(
        f"/api/v1/billing/orgs/{auth_org.id}/dev-upgrade", 
        json={"plan_id": "pro"},
        headers=auth_headers
    )
    assert resp.status_code == 200
    assert resp.json()["status"] == "success"

    # 3. Verify updated to pro
    resp = await client.get(f"/api/v1/billing/orgs/{auth_org.id}/subscription", headers=auth_headers)
    assert resp.json()["plan"] == "pro"
    
@pytest.mark.asyncio
async def test_dev_upgrade_invalid_plan(client, auth_headers, auth_org):
    """Test upgrading to a non-existent plan fails"""
    resp = await client.post(
        f"/api/v1/billing/orgs/{auth_org.id}/dev-upgrade", 
        json={"plan_id": "super-mega-ultra-plan"},
        headers=auth_headers
    )
    assert resp.status_code == 400
