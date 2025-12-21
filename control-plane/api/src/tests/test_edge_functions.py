import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
import pytest

# Add source directory to path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

# Import app after modifying sys.path
from main import app

client = TestClient(app)

@patch("api.v1.functions.FunctionsService")
@patch("api.v1.functions.validate_project_access")
def test_list_functions(mock_validate, mock_service_cls):
    # Setup mock
    mock_service = MagicMock()
    mock_service_cls.return_value = mock_service
    mock_service.list_functions.return_value = [
        {"name": "hello", "runtime": "deno", "id": "123"}
    ]
    
    # Execute
    response = client.get("/api/v1/projects/proj-1/functions")
    
    # Assert
    assert response.status_code == 200
    assert response.json() == [{"name": "hello", "runtime": "deno", "id": "123"}]
    mock_service.list_functions.assert_called_once()
    mock_validate.assert_called_once_with("proj-1")

@patch("api.v1.functions.FunctionsService")
@patch("api.v1.functions.validate_project_access")
def test_create_function(mock_validate, mock_service_cls):
    mock_service = MagicMock()
    mock_service_cls.return_value = mock_service
    mock_service.create_function.return_value = {"id": "123", "name": "new-func"}
    
    payload = {
        "name": "new-func",
        "code": "console.log('test')"
    }
    
    response = client.post("/api/v1/projects/proj-1/functions", json=payload)
    
    assert response.status_code == 200
    assert response.json() == {"id": "123", "name": "new-func"}
    mock_service.create_function.assert_called_once()
    args, kwargs = mock_service.create_function.call_args
    assert kwargs['name'] == "new-func"
    assert kwargs['code'] == "console.log('test')"
    assert kwargs['runtime'] == "deno"
    assert kwargs['version'] == "1.0.0"

@patch("api.v1.functions.FunctionsService")
@patch("api.v1.functions.validate_project_access")
def test_get_function(mock_validate, mock_service_cls):
    mock_service = MagicMock()
    mock_service.get_function.return_value = {"name": "hello", "code": "..."}
    mock_service_cls.return_value = mock_service
    
    response = client.get("/api/v1/projects/proj-1/functions/hello")
    
    assert response.status_code == 200
    assert response.json() == {"name": "hello", "code": "..."}
    mock_service.get_function.assert_called_once_with("hello")

@patch("api.v1.functions.FunctionsService")
@patch("api.v1.functions.validate_project_access")
def test_update_function(mock_validate, mock_service_cls):
    mock_service = MagicMock()
    mock_service_cls.return_value = mock_service
    mock_service.update_function.return_value = {"success": True}
    
    payload = {"code": "new code"}
    response = client.put("/api/v1/projects/proj-1/functions/hello", json=payload)
    
    assert response.status_code == 200
    # Match the actual call signature including default version=None
    mock_service.update_function.assert_called_once()
    args, kwargs = mock_service.update_function.call_args
    assert kwargs['function_name'] == "hello"
    assert kwargs['code'] == "new code"

@patch("api.v1.functions.FunctionsService")
@patch("api.v1.functions.validate_project_access")
def test_delete_function(mock_validate, mock_service_cls):
    mock_service = MagicMock()
    mock_service_cls.return_value = mock_service
    mock_service.delete_function.return_value = {"success": True}
    
    response = client.delete("/api/v1/projects/proj-1/functions/hello")
    
    assert response.status_code == 200
    mock_service.delete_function.assert_called_once_with("hello")
