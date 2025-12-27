from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from services.database_service import DatabaseService
from services.database_service import DatabaseService
from api.v1.utils import verify_project_access
from api.v1.deps import get_db, get_current_user
from sqlalchemy.orm import Session
from models.user import User

router = APIRouter()

class SQLQuery(BaseModel):
    sql: str

class PolicyCreate(BaseModel):
    policy_name: str
    command: str = "ALL"  # SELECT, INSERT, UPDATE, DELETE, ALL
    roles: List[str] = ["public"]
    using_expression: Optional[str] = None
    check_expression: Optional[str] = None

class PolicyUpdate(BaseModel):
    policy_name: Optional[str] = None
    command: Optional[str] = None
    roles: Optional[List[str]] = None
    using_expression: Optional[str] = None
    check_expression: Optional[str] = None

@router.get("/{project_id}/tables")
@router.get("/{project_id}/tables")
def list_tables(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all tables in the project database"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_tables()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/sql")
@router.post("/{project_id}/sql")
def execute_sql(
    project_id: str,
    query: SQLQuery,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Execute SQL query on project database"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        result = db_service.execute_query(query.sql)
        if result.get("error"):
            return {"success": False, **result}
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}/tables/{table_name}/schema")
@router.get("/{project_id}/tables/{table_name}/schema")
def get_table_schema(
    project_id: str,
    table_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get schema for a specific table"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_table_schema(table_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}/tables/{table_name}/data")
@router.get("/{project_id}/tables/{table_name}/data")
def get_table_data(
    project_id: str,
    table_name: str,
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get sample data from a table"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_table_data(table_name, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# RLS Policy Management

@router.get("/{project_id}/tables/{table_name}/policies")
@router.get("/{project_id}/tables/{table_name}/policies")
def list_rls_policies(
    project_id: str,
    table_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all RLS policies for a table"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_rls_policies(table_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/tables/{table_name}/policies")
@router.post("/{project_id}/tables/{table_name}/policies")
def create_rls_policy(
    project_id: str,
    table_name: str,
    policy: PolicyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new RLS policy"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        result = db_service.create_rls_policy(
            table_name=table_name,
            policy_name=policy.policy_name,
            command=policy.command,
            roles=policy.roles,
            using_expr=policy.using_expression,
            check_expr=policy.check_expression
        )
        if result.get("error"):
            return {"success": False, **result}
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}/tables/{table_name}/policies/{policy_name}")
@router.get("/{project_id}/tables/{table_name}/policies/{policy_name}")
def get_rls_policy(
    project_id: str,
    table_name: str,
    policy_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get details of a specific RLS policy"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        policies = db_service.get_rls_policies(table_name)
        policy = next((p for p in policies if p["policy_name"] == policy_name), None)
        if not policy:
            raise HTTPException(status_code=404, detail="Policy not found")
        return policy
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{project_id}/tables/{table_name}/policies/{policy_name}")
@router.put("/{project_id}/tables/{table_name}/policies/{policy_name}")
def update_rls_policy(
    project_id: str,
    table_name: str,
    policy_name: str,
    policy: PolicyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update an RLS policy"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        result = db_service.update_rls_policy(
            table_name=table_name,
            policy_name=policy_name,
            new_policy_name=policy.policy_name,
            command=policy.command,
            roles=policy.roles,
            using_expr=policy.using_expression,
            check_expr=policy.check_expression
        )
        if result.get("error"):
            return {"success": False, **result}
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{project_id}/tables/{table_name}/policies/{policy_name}")
@router.delete("/{project_id}/tables/{table_name}/policies/{policy_name}")
def delete_rls_policy(
    project_id: str,
    table_name: str,
    policy_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete an RLS policy"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        result = db_service.delete_rls_policy(table_name, policy_name)
        if result.get("error"):
            return {"success": False, **result}
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/tables/{table_name}/rls/enable")
@router.post("/{project_id}/tables/{table_name}/rls/enable")
def enable_rls(
    project_id: str,
    table_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Enable RLS on a table"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        result = db_service.enable_rls(table_name)
        if result.get("error"):
            return {"success": False, **result}
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/tables/{table_name}/rls/disable")
@router.post("/{project_id}/tables/{table_name}/rls/disable")
def disable_rls(
    project_id: str,
    table_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Disable RLS on a table"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        result = db_service.disable_rls(table_name)
        if result.get("error"):
            return {"success": False, **result}
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Table Exploration

@router.get("/{project_id}/tables/{table_name}/constraints")
@router.get("/{project_id}/tables/{table_name}/constraints")
def get_table_constraints(
    project_id: str,
    table_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all constraints for a table"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_table_constraints(table_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}/tables/{table_name}/indexes")
@router.get("/{project_id}/tables/{table_name}/indexes")
def get_table_indexes(
    project_id: str,
    table_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all indexes for a table"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_table_indexes(table_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}/tables/{table_name}/size")
@router.get("/{project_id}/tables/{table_name}/size")
def get_table_size(
    project_id: str,
    table_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get size information for a table"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_table_size(table_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Realtime Management

@router.post("/{project_id}/tables/{table_name}/realtime/enable")
def enable_realtime(
    project_id: str,
    table_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Enable realtime replication for a table"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        result = db_service.enable_realtime(table_name)
        if result.get("error"):
            return {"success": False, **result}
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/tables/{table_name}/realtime/disable")
def disable_realtime(
    project_id: str,
    table_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Disable realtime replication for a table"""
    verify_project_access(project_id, db, current_user)
    try:
        db_service = DatabaseService(project_id)
        result = db_service.disable_realtime(table_name)
        if result.get("error"):
            return {"success": False, **result}
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
