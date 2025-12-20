import sys
import os
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

# Add source directory to path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from services.provisioning_coolify import CoolifyProvisioner

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise Exception(f"HTTP Error: {self.status_code}")

@pytest.fixture
def provisioner():
    return CoolifyProvisioner("http://coolify.mock", "mock-token")

@patch("httpx.Client")
def test_provision_project(mock_client_cls, provisioner):
    # Mock Client instance
    mock_client = MagicMock()
    mock_client_cls.return_value.__enter__.return_value = mock_client

    # Define mock responses for sequential calls
    # 1. _find_resource_by_name -> [] (Application doesn't exist)
    # 2. _get_first_server -> [{"uuid": "server-1"}]
    # 3. _ensure_project_and_env -> GET projects -> [{"name": "Auth", "uuid": "p1"}] (Target doesn't exist)
    # 4. _ensure_project_and_env -> POST project -> {"uuid": "proj-users", "name": "Supalove Users"}
    # 5. POST application -> {"uuid": "app-1"}
    # 6. POST env var 1
    # 7. POST env var 2
    # 8. POST env var 3
    # 9. POST deploy

    def side_effect(method, url, **kwargs):
        if "/api/v1/resources" in url:
            return MockResponse([])
        if "/api/v1/servers" in url:
            return MockResponse([{"uuid": "server-1"}])
        if "/api/v1/projects" in url and method == "GET":
            return MockResponse([]) # No match for target
        if "/api/v1/projects" in url and method == "POST":
            return MockResponse({"uuid": "proj-users", "name": "Supalove Users"})
        if "/api/v1/applications/compose" in url:
            return MockResponse({"uuid": "app-1"})
        if "/envs" in url:
            return MockResponse({})
        if "/deploy" in url:
            return MockResponse({"deployment_uuid": "dep-1"})
        if method == "PATCH" and "/api/v1/applications/app-1" in url:
            # For custom domain update
             return MockResponse({"uuid": "app-1", "fqdn": "custom.com"})
        return MockResponse({}, 404)

    mock_client.request.side_effect = side_effect

    # Run provision
    result = provisioner.provision_project("test-123", {"DB_PASSWORD": "pass"})

    assert result["api_url"] == "https://project-test-123.coolify.infra"
    assert "db-test-123" in result["db_url"]
    
    # Verify key calls
    # Check if app was created
    create_call = [call for call in mock_client.request.call_args_list if "/api/v1/applications/compose" in call[0][1]]
    assert len(create_call) == 1
    assert create_call[0][0][1].endswith("/api/v1/applications/compose")
    
    # Check if deployed
    deploy_call = [call for call in mock_client.request.call_args_list if "/deploy" in call[0][1]]
    assert len(deploy_call) == 1
    assert "app-1" in deploy_call[0][0][1]

@patch("httpx.Client")
def test_stop_project(mock_client_cls, provisioner):
    mock_client = MagicMock()
    mock_client_cls.return_value.__enter__.return_value = mock_client

    # 1. find resource -> found
    # 2. stop
    
    def side_effect(method, url, **kwargs):
        if "/api/v1/resources" in url:
            return MockResponse([{"name": "project-test-123", "uuid": "app-1"}])
        if "/stop" in url:
            return MockResponse({"status": "stopped"})
        return MockResponse({}, 404)

    mock_client.request.side_effect = side_effect

    provisioner.stop_project("test-123")
    
    # Verify stop call
    stop_call = [call for call in mock_client.request.call_args_list if "/stop" in call[0][1]]
    assert len(stop_call) == 1
    assert "app-1" in stop_call[0][0][1]

@patch("httpx.Client")
def test_provision_project_custom_domain(mock_client_cls, provisioner):
    mock_client = MagicMock()
    mock_client_cls.return_value.__enter__.return_value = mock_client

    def side_effect(method, url, **kwargs):
        if "/api/v1/resources" in url: return MockResponse([])
        if "/api/v1/servers" in url: return MockResponse([{"uuid": "server-1"}])
        if "/api/v1/projects" in url:
            if method == "GET": return MockResponse([])
            return MockResponse({"uuid": "proj-users", "name": "Supalove Users"})
        if "/api/v1/applications/compose" in url: return MockResponse({"uuid": "app-1"})
        if "/envs" in url: return MockResponse({})
        if "/deploy" in url: return MockResponse({"deployment_uuid": "dep-1"})
        
        # Verify PATCH call for custom domain
        if method == "PATCH" and "/api/v1/applications/app-1" in url:
            return MockResponse({"uuid": "app-1", "fqdn": "custom.com"})
            
        return MockResponse({}, 404)

    mock_client.request.side_effect = side_effect

    # Run provision with custom domain
    result = provisioner.provision_project("test-domain", {"DB_PASSWORD": "pass"}, custom_domain="myapp.com")

    # Verify return URL is the custom domain
    assert result["api_url"] == "https://myapp.com"
    
    # Verify PATCH call was made
    patch_calls = [call for call in mock_client.request.call_args_list if call[0][0] == "PATCH" and "/api/v1/applications/app-1" in call[0][1]]
    patch_call = [call for call in mock_client.request.call_args_list if call[0][0] == "PATCH"]
    assert len(patch_call) == 1
    assert patch_call[0][1]['json']['fqdn'] == "myapp.com"
