from fastapi import APIRouter
from services.project_service import create_project

router = APIRouter()

@router.post("/")
def create():
    return create_project()
