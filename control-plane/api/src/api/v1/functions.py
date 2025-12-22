from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, Dict, Any
from services.functions_service import FunctionsService
from services.functions_service import FunctionsService
from api.v1.utils import verify_project_access
from api.v1.deps import get_db, get_current_user
from sqlalchemy.orm import Session
from models.user import User

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
@router.get("/{project_id}/functions")
def list_functions(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all edge functions for a project"""
    verify_project_access(project_id, db, current_user)
    try:
        service = FunctionsService(project_id)
        return service.list_functions()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/functions")
@router.post("/{project_id}/functions")
def create_function(
    project_id: str,
    function: FunctionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Deploy a new edge function"""
    verify_project_access(project_id, db, current_user)
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
@router.get("/{project_id}/functions/{function_name}")
def get_function(
    project_id: str,
    function_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get function details and code"""
    verify_project_access(project_id, db, current_user)
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
@router.put("/{project_id}/functions/{function_name}")
def update_function(
    project_id: str,
    function_name: str,
    function: FunctionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update function code"""
    verify_project_access(project_id, db, current_user)
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
@router.delete("/{project_id}/functions/{function_name}")
def delete_function(
    project_id: str,
    function_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete an edge function"""
    verify_project_access(project_id, db, current_user)
    try:
        service = FunctionsService(project_id)
        return service.delete_function(function_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/functions/{function_name}/invoke")
@router.post("/{project_id}/functions/{function_name}/invoke")
def invoke_function(
    project_id: str,
    function_name: str,
    invoke: FunctionInvoke,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Test invoke a function"""
    verify_project_access(project_id, db, current_user)
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
