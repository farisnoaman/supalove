import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_project_lifecycle(client: AsyncClient, auth_headers, db):
    # 1. Create Org (Mocked or existing - assuming user has one from conftest or we create one here)
    # Since we use rollback transaction, we can insert data safely.
    # But for simplicity, let's assume valid session user logic or mock verifying access.
    # The auth_headers mocks a user "test-user-id".
    # We need to ensure an Org exists for this user.
    
    # Setup: Create Org and Member
    from models.organization import Organization
    from models.org_member import OrgMember
    from models.user import User
    import uuid
    
    user_id = "test-user-id"
    org_id = str(uuid.uuid4())
    
    # Sync insert to DB using the session fixture
    user = User(id=user_id, email="test@supalove.local", is_active=True)
    db.merge(user) # Merge in case exists
    
    org = Organization(id=org_id, name="Test Org", plan="free", created_by_user_id=user_id)
    db.add(org)
    
    member = OrgMember(org_id=org_id, user_id=user_id, role="owner")
    db.add(member)
    
    # Also add Quota
    from models.resource_quota import ResourceQuota
    quota = ResourceQuota(org_id=org_id, max_projects=3, max_db_size_mb=500, max_storage_mb=1000)
    db.add(quota)
    
    db.flush() # Send to DB so API can see it (if sharing session)
    # Note: For `client` to see this, it MUST share the same db session. 
    # Our `client` fixture overrides `get_db` to use `yield db` (the test session).
    # So this data is visible!

    # 2. Create Project
    payload = {"name": "Test Project 1", "org_id": org_id, "region": "us-east-1"}
    resp = await client.post("/api/v1/projects", json=payload, headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Test Project 1"
    project_id = data["id"]
    
    # 3. List Projects
    resp = await client.get(f"/api/v1/projects?org_id={org_id}", headers=auth_headers)
    assert resp.status_code == 200
    projects = resp.json()
    assert len(projects) == 1
    assert projects[0]["id"] == project_id
    
    # 4. Quota Enforcement Test
    # Create 2 more (Total 3)
    await client.post("/api/v1/projects", json={"name": "P2", "org_id": org_id}, headers=auth_headers)
    await client.post("/api/v1/projects", json={"name": "P3", "org_id": org_id}, headers=auth_headers)
    
    # Create 4th -> Should fail
    resp = await client.post("/api/v1/projects", json={"name": "P4", "org_id": org_id}, headers=auth_headers)
    assert resp.status_code == 402
    assert "limit reached" in resp.json()["detail"]
    
    # 5. Delete Project
    resp = await client.delete(f"/api/v1/projects/{project_id}", headers=auth_headers)
    assert resp.status_code == 200
    
    # 6. Verify Delete
    resp = await client.get(f"/api/v1/projects?org_id={org_id}", headers=auth_headers)
    assert len(resp.json()) == 2
