import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
import pytest

# Add source directory to path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from main import app

client = TestClient(app)

@patch("api.v1.database.DatabaseService")
@patch("api.v1.database.validate_project_access")
def test_list_rls_policies(mock_validate, mock_service_cls):
    mock_service = MagicMock()
    mock_service_cls.return_value = mock_service
    mock_service.get_rls_policies.return_value = [
        {"policy_name": "p1", "command": "ALL", "roles": ["public"]}
    ]
    
    response = client.get("/api/v1/projects/proj-1/tables/users/policies")
    
    assert response.status_code == 200
    assert response.json() == [{"policy_name": "p1", "command": "ALL", "roles": ["public"]}]
    mock_service.get_rls_policies.assert_called_once_with("users")

@patch("api.v1.database.DatabaseService")
@patch("api.v1.database.validate_project_access")
def test_create_rls_policy(mock_validate, mock_service_cls):
    mock_service = MagicMock()
    mock_service_cls.return_value = mock_service
    mock_service.create_rls_policy.return_value = {"success": True}
    
    payload = {
        "policy_name": "new_policy",
        "command": "SELECT",
        "roles": ["authenticated"],
        "using_expression": "auth.uid() = id"
    }
    
    response = client.post("/api/v1/projects/proj-1/tables/users/policies", json=payload)
    
    assert response.status_code == 200
    mock_service.create_rls_policy.assert_called_once()
    args, kwargs = mock_service.create_rls_policy.call_args
    assert kwargs['table_name'] == "users"
    assert kwargs['policy_name'] == "new_policy"
    assert kwargs['using_expr'] == "auth.uid() = id"

@patch("api.v1.database.DatabaseService")
@patch("api.v1.database.validate_project_access")
def test_update_rls_policy(mock_validate, mock_service_cls):
    mock_service = MagicMock()
    mock_service_cls.return_value = mock_service
    mock_service.update_rls_policy.return_value = {"success": True}
    
    payload = {
        "policy_name": "updated_name",
        "using_expression": "true"
    }
    
    response = client.put("/api/v1/projects/proj-1/tables/users/policies/old_policy", json=payload)
    
    assert response.status_code == 200
    mock_service.update_rls_policy.assert_called_once()
    args, kwargs = mock_service.update_rls_policy.call_args
    assert kwargs['table_name'] == "users"
    assert kwargs['policy_name'] == "old_policy"
    assert kwargs['new_policy_name'] == "updated_name"

@patch("api.v1.database.DatabaseService")
@patch("api.v1.database.validate_project_access")
def test_delete_rls_policy(mock_validate, mock_service_cls):
    mock_service = MagicMock()
    mock_service_cls.return_value = mock_service
    mock_service.delete_rls_policy.return_value = {"success": True}
    
    response = client.delete("/api/v1/projects/proj-1/tables/users/policies/p1")
    
    assert response.status_code == 200
    mock_service.delete_rls_policy.assert_called_once_with("users", "p1")

@patch("api.v1.database.DatabaseService")
@patch("api.v1.database.validate_project_access")
def test_enable_rls(mock_validate, mock_service_cls):
    mock_service = MagicMock()
    mock_service_cls.return_value = mock_service
    mock_service.enable_rls.return_value = {"success": True}
    
    response = client.post("/api/v1/projects/proj-1/tables/users/rls/enable")
    
    assert response.status_code == 200
    mock_service.enable_rls.assert_called_once_with("users")

@patch("api.v1.database.DatabaseService")
@patch("api.v1.database.validate_project_access")
def test_get_table_constraints(mock_validate, mock_service_cls):
    mock_service = MagicMock()
    mock_service_cls.return_value = mock_service
    mock_service.get_table_constraints.return_value = [{"constraint_name": "pk_users"}]
    
    response = client.get("/api/v1/projects/proj-1/tables/users/constraints")
    
    assert response.status_code == 200
    assert response.json() == [{"constraint_name": "pk_users"}]
    mock_service.get_table_constraints.assert_called_once_with("users")
