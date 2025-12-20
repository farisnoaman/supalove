from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.project_service import (
    create_project,
    get_projects,
    get_project_by_id,
    stop_project,
    start_project,
    delete_project,
    restore_project,
)
from services.database_service import DatabaseService

router = APIRouter()

class SQLQuery(BaseModel):
    sql: str

@router.get("/projects")
def list_projects():
    return get_projects()

@router.get("/projects/{project_id}")
def get_project(project_id: str):
    project = get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/projects")
def create():
    return create_project()

@router.post("/projects/{project_id}/stop")
def stop(project_id: str):
    project = stop_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "stopped", "project_id": project.id}

@router.post("/projects/{project_id}/start")
def start(project_id: str):
    project = start_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "running", "project_id": project.id}

@router.post("/projects/{project_id}/restore")
def restore(project_id: str):
    try:
        project = restore_project(project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return {"status": "stopped", "project_id": project.id}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archived project not found")
    except FileExistsError:
        raise HTTPException(status_code=400, detail="Project is already active")


@router.delete("/projects/{project_id}")
def delete(project_id: str):
    project = delete_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "deleted", "project_id": project.id}

# Database Management Endpoints

@router.get("/projects/{project_id}/tables")
def list_tables(project_id: str):
    """List all tables in the project database"""
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_tables()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/projects/{project_id}/sql")
def execute_sql(project_id: str, query: SQLQuery):
    """Execute SQL query on project database"""
    try:
        db_service = DatabaseService(project_id)
        result = db_service.execute_query(query.sql)
        if result.get("error"):
            return {"success": False, **result}
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/projects/{project_id}/tables/{table_name}/schema")
def get_table_schema(project_id: str, table_name: str):
    """Get schema for a specific table"""
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_table_schema(table_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/projects/{project_id}/tables/{table_name}/data")
def get_table_data(project_id: str, table_name: str, limit: int = 50):
    """Get sample data from a table"""
    try:
        db_service = DatabaseService(project_id)
        return db_service.get_table_data(table_name, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
