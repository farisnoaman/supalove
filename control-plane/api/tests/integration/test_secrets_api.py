import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session
from models.project import Project, ProjectStatus

@pytest.mark.asyncio
async def test_secrets_management(client: AsyncClient, auth_headers, db: Session):
    # Setup deps: Org and Cluster
    from models.organization import Organization
    from models.cluster import Cluster, ClusterStatus, ClusterType
    from models.user import User
    from models.org_member import OrgMember

    # Get test user (created by auth_headers fixture)
    user = db.query(User).filter(User.email == "faris1@faris.com").first()
    
    org = Organization(id="test-org-secrets", name="Secrets Org", slug="secrets-org")
    cluster = Cluster(id="test-cluster-secrets", type=ClusterType.global_shared, status=ClusterStatus.running)
    
    db.add(org)
    db.add(cluster)
    db.flush()
    
    # Grant access
    member = OrgMember(org_id=org.id, user_id=user.id, role="owner")
    db.add(member)
    
    db.commit()

    from models.project import Project, ProjectStatus, ProjectPlan
    
    # 1. Create a dummy project directly in DB
    project_id = "secret-test-proj"
    project = Project(
        id=project_id,
        name="Secrets Test",
        org_id="test-org-secrets",
        cluster_id="test-cluster-secrets",
        status=ProjectStatus.RUNNING,
        plan=ProjectPlan.shared
    )
    db.add(project)
    db.commit()
    
    # Debug: Confirm project exists in session
    saved_p = db.query(Project).filter(Project.id == project_id).first()
    assert saved_p is not None, "Project failed to save to DB session"
    
    # 2. Add an initial secret via API
    response = await client.post(
        f"/api/v1/projects/{project_id}/secrets",
        json={"key": "TEST_KEY", "value": "test_value"},
        headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["TEST_KEY"] == "test_value"
    
    # 3. List secrets
    response = await client.get(
        f"/api/v1/projects/{project_id}/secrets",
        headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["TEST_KEY"] == "test_value"
    
    # 4. Update secret
    response = await client.post(
        f"/api/v1/projects/{project_id}/secrets",
        json={"key": "TEST_KEY", "value": "new_value"},
        headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["TEST_KEY"] == "new_value"
    
    # 5. Delete secret
    response = await client.delete(
        f"/api/v1/projects/{project_id}/secrets/TEST_KEY",
        headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert "TEST_KEY" not in data
    
    # Cleanup
    db.delete(project)
    db.commit()
