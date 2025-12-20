import secrets
from sqlalchemy.orm import Session
from models.project_secret import ProjectSecret

def generate_project_secrets(
    db: Session,
    project_id: str
):
    # Generate a unique port for this project (starting from 5433 to avoid conflicts)
    # Use the last 4 characters of project_id to generate a port number
    port_suffix = abs(hash(project_id)) % 1000 + 5433
    db_port = str(port_suffix)

    secrets_map = {
        "JWT_SECRET": secrets.token_hex(32),
        "DB_PASSWORD": secrets.token_urlsafe(24),
        "ANON_KEY": secrets.token_urlsafe(32),
        "SERVICE_ROLE_KEY": secrets.token_urlsafe(48),
        "DB_PORT": db_port,
        "REST_PORT": str(int(db_port) + 1000),  # REST port is DB port + 1000
        "REALTIME_PORT": str(int(db_port) + 2000),  # Realtime port is DB port + 2000
    }

    for key, value in secrets_map.items():
        db.add(ProjectSecret(
            project_id=project_id,
            key=key,
            value=value
        ))

    db.commit()
    return secrets_map
