import os
import uuid
import httpx
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from models.edge_function import EdgeFunction
from core.database import SessionLocal
from models.project import Project

class FunctionsService:
    """
    Service for managing edge functions.
    Stores function code in the database and manages deployment to the Deno runtime.
    """
    
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.functions_dir = self._get_functions_directory()
    
    def _get_functions_directory(self) -> Path:
        """Get the directory where function code is stored for this project"""
        # For local development, store in data-plane/projects/{project_id}/functions
        base_path = Path(__file__).resolve().parents[5] / "data-plane" / "projects" / self.project_id / "functions"
        base_path.mkdir(parents=True, exist_ok=True)
        return base_path
    
    def _get_function_url(self, function_name: str) -> Optional[str]:
        """Get the URL for invoking a function"""
        # TODO: Get the actual function port from the project's deployment
        # For now, assuming functions service runs on a calculated port
        db = SessionLocal()
        try:
            from models.project_secret import ProjectSecret
            port_secret = db.query(ProjectSecret).filter(
                ProjectSecret.project_id == self.project_id,
                ProjectSecret.key == "FUNCTIONS_PORT"
            ).first()
            
            if port_secret:
                return f"http://localhost:{port_secret.value}/{function_name}"
            return None
        finally:
            db.close()
    
    def list_functions(self) -> List[Dict[str, Any]]:
        """List all edge functions for the project"""
        db = SessionLocal()
        try:
            functions = db.query(EdgeFunction).filter(
                EdgeFunction.project_id == self.project_id
            ).order_by(EdgeFunction.created_at.desc()).all()
            
            return [
                {
                    "id": f.id,
                    "name": f.name,
                    "runtime": f.runtime,
                    "version": f.version,
                    "created_at": f.created_at.isoformat() if f.created_at else None,
                    "updated_at": f.updated_at.isoformat() if f.updated_at else None,
                }
                for f in functions
            ]
        finally:
            db.close()
    
    def get_function(self, function_name: str) -> Optional[Dict[str, Any]]:
        """Get a specific function by name"""
        db = SessionLocal()
        try:
            func = db.query(EdgeFunction).filter(
                EdgeFunction.project_id == self.project_id,
                EdgeFunction.name == function_name
            ).first()
            
            if not func:
                return None
            
            return {
                "id": func.id,
                "name": func.name,
                "code": func.code,
                "runtime": func.runtime,
                "version": func.version,
                "created_at": func.created_at.isoformat() if func.created_at else None,
                "updated_at": func.updated_at.isoformat() if func.updated_at else None,
            }
        finally:
            db.close()
    
    def create_function(
        self,
        name: str,
        code: str,
        runtime: str = "deno",
        version: str = "1.0.0"
    ) -> Dict[str, Any]:
        """Create a new edge function"""
        db = SessionLocal()
        try:
            # Check if function already exists
            existing = db.query(EdgeFunction).filter(
                EdgeFunction.project_id == self.project_id,
                EdgeFunction.name == name
            ).first()
            
            if existing:
                raise ValueError(f"Function '{name}' already exists")
            
            # Create function record
            func = EdgeFunction(
                id=str(uuid.uuid4()),
                project_id=self.project_id,
                name=name,
                code=code,
                runtime=runtime,
                version=version
            )
            
            db.add(func)
            db.commit()
            db.refresh(func)
            
            # Write function code to file
            self._write_function_file(name, code)
            
            return {
                "id": func.id,
                "name": func.name,
                "runtime": func.runtime,
                "version": func.version,
                "created_at": func.created_at.isoformat() if func.created_at else None,
            }
        finally:
            db.close()
    
    def update_function(
        self,
        function_name: str,
        code: Optional[str] = None,
        version: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update an existing edge function"""
        db = SessionLocal()
        try:
            func = db.query(EdgeFunction).filter(
                EdgeFunction.project_id == self.project_id,
                EdgeFunction.name == function_name
            ).first()
            
            if not func:
                raise ValueError(f"Function '{function_name}' not found")
            
            if code is not None:
                func.code = code
                self._write_function_file(function_name, code)
            
            if version is not None:
                func.version = version
            
            func.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(func)
            
            return {
                "id": func.id,
                "name": func.name,
                "runtime": func.runtime,
                "version": func.version,
                "updated_at": func.updated_at.isoformat() if func.updated_at else None,
            }
        finally:
            db.close()
    
    def delete_function(self, function_name: str) -> Dict[str, str]:  
        """Delete an edge function"""
        db = SessionLocal()
        try:
            func = db.query(EdgeFunction).filter(
                EdgeFunction.project_id == self.project_id,
                EdgeFunction.name == function_name
            ).first()
            
            if not func:
                raise ValueError(f"Function '{function_name}' not found")
            
            # Delete from database
            db.delete(func)
            db.commit()
            
            # Delete function file
            self._delete_function_file(function_name)
            
            return {"message": f"Function '{function_name}' deleted successfully"}
        finally:
            db.close()
    
    def invoke_function(
        self,
        function_name: str,
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Invoke an edge function"""
        function_url = self._get_function_url(function_name)
        
        if not function_url:
            return {
                "error": "Function runtime not available. Edge functions service may not be running.",
                "status_code": 503
            }
        
        try:
            # Make HTTP request to the function runtime
            with httpx.Client(timeout=30.0) as client:
                response = client.post(
                    function_url,
                    json=payload or {},
                    headers=headers or {}
                )
                
                return {
                    "status_code": response.status_code,
                    "headers": dict(response.headers),
                    "body": response.text,
                    "json": response.json() if response.headers.get("content-type", "").startswith("application/json") else None
                }
        except httpx.RequestError as e:
            return {
                "error": f"Failed to invoke function: {str(e)}",
                "status_code": 500
            }
    
    def _write_function_file(self, name: str, code: str):
        """Write function code to a file"""
        file_path = self.functions_dir / f"{name}.ts"
        file_path.write_text(code, encoding="utf-8")
    
    def _delete_function_file(self, name: str):
        """Delete function code file"""
        file_path = self.functions_dir / f"{name}.ts"
        if file_path.exists():
            file_path.unlink()
