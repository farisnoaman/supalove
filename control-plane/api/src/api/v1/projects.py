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
from api.v1.utils import validate_project_access

router = APIRouter()

class ProjectCreate(BaseModel):
    custom_domain: str = None
    name: str = None

@router.get("")
def list_projects():
    return get_projects()

@router.get("/{project_id}")
def get_project(project_id: str):
    validate_project_access(project_id)
    project = get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("")
def create(project: ProjectCreate = None):
    custom_domain = project.custom_domain if project else None
    name = project.name if project else None
    return create_project(custom_domain=custom_domain, name=name)

@router.post("/{project_id}/stop")
def stop(project_id: str):
    validate_project_access(project_id)
    project = stop_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "stopped", "project_id": project.id}

@router.post("/{project_id}/start")
def start(project_id: str):
    validate_project_access(project_id)
    project = start_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "running", "project_id": project.id}

@router.post("/{project_id}/restore")
def restore(project_id: str):
    validate_project_access(project_id)
    try:
        project = restore_project(project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return {"status": "stopped", "project_id": project.id}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archived project not found")
    except FileExistsError:
        raise HTTPException(status_code=400, detail="Project is already active")

@router.delete("/{project_id}")
def delete(project_id: str):
    validate_project_access(project_id)
    project = delete_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "deleted", "project_id": project.id}
