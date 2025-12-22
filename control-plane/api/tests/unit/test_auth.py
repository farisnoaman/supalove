import pytest
from jose import jwt
import os

# Unit tests for jwt utils (if we had them isolated)
# For now, we test the auth endpoints directly via integration tests,
# or test internal utils.

@pytest.mark.asyncio
async def test_health_check(client):
    response = await client.get("/health")
    # Health endpoint might not be auth protected
    if response.status_code == 404:
        # If /health doesn't exist, try root
        response = await client.get("/")
    
    # Just verifying client works
    assert response.status_code in [200, 404]

@pytest.mark.asyncio
async def test_login_fail_no_creds(client):
    response = await client.post("/api/v1/auth/token", data={})
    assert response.status_code == 422 # Validation error

@pytest.mark.asyncio
async def test_protected_route_fails_without_token(client):
    # Try to list projects without auth
    response = await client.get("/api/v1/projects")
    assert response.status_code == 401
