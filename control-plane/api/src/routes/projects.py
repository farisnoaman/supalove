from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import secrets

from core.database import get_db
from models.project import Project
from models.project_secret import ProjectSecret

router = APIRouter(prefix="/v1/projects", tags=["projects"])


@router.post("")
def create_project(db: Session = Depends(get_db)):
    project_id = secrets.token_hex(6)

    project = Project(id=project_id, status="running")
    db.add(project)

    secrets_map = {
        "JWT_SECRET": secrets.token_hex(32),
        "DB_PASSWORD": secrets.token_hex(16),
        "ANON_KEY": secrets.token_hex(16),
        "SERVICE_ROLE_KEY": secrets.token_hex(32),
    }

    for key, value in secrets_map.items():
        db.add(
            ProjectSecret(
                project_id=project_id,
                key=key,
                value=value,
            )
        )

    db.commit()

    return {
        "project_id": project_id,
        "status": "running",
        "api_url": f"http://localhost:{project_id}",
    }
