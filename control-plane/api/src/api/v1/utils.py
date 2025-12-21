from fastapi import HTTPException, Depends
from core.database import SessionLocal
from models.project import Project

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def validate_project_access(project_id: str, owner_id: str = None):
    """
    Middleware/Dependency to validate that a project exists and 
    optionally matches the owner_id.
    """
    db = SessionLocal()
    try:
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        
        if owner_id and project.owner_id != owner_id:
            raise HTTPException(status_code=403, detail="Access denied to this project")
            
        return project
    finally:
        db.close()
