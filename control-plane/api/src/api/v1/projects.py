from fastapi import APIRouter, HTTPException
from services.project_service import (
    create_project,
    stop_project,
    start_project,
    delete_project,
    restore_project,
)

router = APIRouter()

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
