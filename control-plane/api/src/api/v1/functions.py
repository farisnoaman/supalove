from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from services.functions_service import FunctionsService
from api.v1.utils import validate_project_access

router = APIRouter()

class FunctionCreate(BaseModel):
    name: str
    code: str
    runtime: str = "deno"
    version: str = "1.0.0"

class FunctionUpdate(BaseModel):
    code: Optional[str] = None
    version: Optional[str] = None

class FunctionInvoke(BaseModel):
    payload: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, str]] = None

@router.get("/{project_id}/functions")
def list_functions(project_id: str):
    """List all edge functions for a project"""
    validate_project_access(project_id)
    try:
        service = FunctionsService(project_id)
        return service.list_functions()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/functions")
def create_function(project_id: str, function: FunctionCreate):
    """Deploy a new edge function"""
    validate_project_access(project_id)
    try:
        service = FunctionsService(project_id)
        return service.create_function(
            name=function.name,
            code=function.code,
            runtime=function.runtime,
            version=function.version
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}/functions/{function_name}")
def get_function(project_id: str, function_name: str):
    """Get function details and code"""
    validate_project_access(project_id)
    try:
        service = FunctionsService(project_id)
        func = service.get_function(function_name)
        if not func:
            raise HTTPException(status_code=404, detail="Function not found")
        return func
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{project_id}/functions/{function_name}")
def update_function(project_id: str, function_name: str, function: FunctionUpdate):
    """Update function code"""
    validate_project_access(project_id)
    try:
        service = FunctionsService(project_id)
        return service.update_function(
            function_name=function_name,
            code=function.code,
            version=function.version
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{project_id}/functions/{function_name}")
def delete_function(project_id: str, function_name: str):
    """Delete an edge function"""
    validate_project_access(project_id)
    try:
        service = FunctionsService(project_id)
        return service.delete_function(function_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/functions/{function_name}/invoke")
def invoke_function(project_id: str, function_name: str, invoke: FunctionInvoke):
    """Test invoke a function"""
    validate_project_access(project_id)
    try:
        service = FunctionsService(project_id)
        result = service.invoke_function(
            function_name=function_name,
            payload=invoke.payload,
            headers=invoke.headers
        )
        
        if result.get("error"):
            raise HTTPException(
                status_code=result.get("status_code", 500),
                detail=result.get("error")
            )
        
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
