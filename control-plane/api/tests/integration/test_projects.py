import uuid
import pytest
from unittest.mock import patch, MagicMock
from httpx import AsyncClient

# Mock provisioning responses
MOCK_PROVISION_OUTPUT = {
    "api_url": "http://mock-api.local",
    "db_url": "postgresql://mock:mock@localhost:5432/mock_db"
}

@pytest.mark.asyncio
@patch("services.project_service.provision_project", return_value=MOCK_PROVISION_OUTPUT)
@patch("services.project_service.provision_shared_project", return_value=MOCK_PROVISION_OUTPUT)
@patch("services.project_service.provision_delete")
async def test_project_lifecycle(mock_delete, mock_shared_provision, mock_provision, client: AsyncClient, auth_headers, db):

    """Full project lifecycle test using existing data.
    
    Uses:
    - User: faris1@faris.com
    - Org: 09c58234-02a0-4731-b7c4-6246c550930b
    """
    # 1. Get User
    from models.user import User
    user = db.query(User).filter(User.email == "faris1@faris.com").first()
    assert user is not None, "Test user faris1@faris.com not found in DB"

    # 2. Get or Create Org & Ensure Quota
    from models.organization import Organization
    from models.org_member import OrgMember
    org_id = "09c58234-02a0-4731-b7c4-6246c550930b"
    org = db.query(Organization).filter(Organization.id == org_id).first()
    
    if not org:
        # Create if missing (fallback mechanism)
        org = Organization(id=org_id, name="Test Org", slug="test-org-existing") # plan='free' removed from model
        db.add(org)
        db.flush()
        
        member = OrgMember(org_id=org_id, user_id=user.id, role="owner")
        db.add(member)

    # Ensure Entitlement (Pro plan for sufficient limits)
    from services.entitlement_service import EntitlementService
    # Manually update entitlement to PRO to ensure we have enough project quota (Free=2, Pro=20)
    
    ent = EntitlementService.get_entitlements(db, org.id)
    if ent.plan_id != "pro":
        ent.plan_id = "pro"
        db.commit()
    
    # Also sync subscription if exists (optional but good for consistency)
    from models.subscription import Subscription
    sub = db.query(Subscription).filter(Subscription.org_id == org.id).first()
    if sub and sub.plan_id != "pro":
        sub.plan_id = "pro"
        db.commit()

    # 3. Create Project
    # Use a random suffix to avoid name collision if running repeatedly
    suffix = str(uuid.uuid4())[:8]
    test_project_name = f"Test Project {suffix}"
    payload = {"name": test_project_name, "org_id": org_id, "region": "us-east-1"}
    
    resp = await client.post("/api/v1/projects", json=payload, headers=auth_headers)
    assert resp.status_code == 200, f"Project creation failed: {resp.text}"
    data = resp.json()
    project_id = data["id"]
    assert data["api_url"] == MOCK_PROVISION_OUTPUT["api_url"]

    # 4. List Projects
    resp = await client.get(f"/api/v1/projects?org_id={org_id}", headers=auth_headers)
    assert resp.status_code == 200
    projects = resp.json()
    assert any(p["id"] == project_id for p in projects)

    # 5. Delete Project (Only the one we created)
    resp = await client.delete(f"/api/v1/projects/{project_id}", headers=auth_headers)
    assert resp.status_code == 200

    # 6. Verify Delete
    resp = await client.get(f"/api/v1/projects?org_id={org_id}", headers=auth_headers)
    assert resp.status_code == 200
    remaining = resp.json()
    assert not any(p["id"] == project_id for p in remaining)
