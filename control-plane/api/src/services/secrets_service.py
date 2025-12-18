import secrets
from sqlalchemy.orm import Session
from models.project_secret import ProjectSecret

def generate_project_secrets(
    db: Session,
    project_id: str
):
    secrets_map = {
        "JWT_SECRET": secrets.token_hex(32),
        "DB_PASSWORD": secrets.token_urlsafe(24),
        "ANON_KEY": secrets.token_urlsafe(32),
        "SERVICE_ROLE_KEY": secrets.token_urlsafe(48),
    }

    for key, value in secrets_map.items():
        db.add(ProjectSecret(
            project_id=project_id,
            key=key,
            value=value
        ))

    db.commit()
