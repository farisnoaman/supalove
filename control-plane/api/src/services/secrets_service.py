import os
import secrets as py_secrets
import socket
from pathlib import Path
from sqlalchemy.orm import Session
from models.project_secret import ProjectSecret
from dotenv import dotenv_values, set_key, unset_key
from services.provisioning_local import BASE_PROJECTS_DIR

def get_project_env_path(project_id: str) -> Path:
    return BASE_PROJECTS_DIR / project_id / ".env"

def get_secrets(project_id: str) -> dict:
    """
    Retrieves secrets from the file system. 
    WARNING: For authoritative secrets, query the database. This is for Provisioner use.
    """
    env_path = get_project_env_path(project_id)
    if not env_path.exists():
        return {}
    return dotenv_values(env_path)

def set_secret(project_id: str, key: str, value: str):
    env_path = get_project_env_path(project_id)
    if not env_path.exists():
        # Create if not exists
        env_path.parent.mkdir(parents=True, exist_ok=True)
        env_path.touch()
    
    set_key(env_path, key, value)
    return get_secrets(project_id)

def delete_secret(project_id: str, key: str):
    env_path = get_project_env_path(project_id)
    if not env_path.exists():
        return {}
        
    unset_key(env_path, key)
    return get_secrets(project_id)

def find_free_port(start_port: int = 5000) -> int:
    port = start_port
    while port < 65535:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("0.0.0.0", port))
                return port
            except socket.error:
                port += 1
    raise Exception("No free ports available")

def generate_project_secrets(db: Session, project_id: str) -> dict:
    """Generates and persists base project secrets: ports, passwords, JWT secrets, API keys."""
    from jose import jwt
    import datetime
    
    # Generate random strings
    db_password = py_secrets.token_hex(16)
    jwt_secret = py_secrets.token_urlsafe(32)
    secret_key_base = py_secrets.token_urlsafe(64)
    
    # Allocate ports (ensuring no conflicts)
    db_port = find_free_port(5500)
    rest_port = find_free_port(db_port + 1)
    realtime_port = find_free_port(rest_port + 1)
    storage_port = find_free_port(realtime_port + 1)
    auth_port = find_free_port(storage_port + 1)
    functions_port = find_free_port(auth_port + 1)
    
    # Generate Supabase-compatible JWT keys
    def generate_supabase_key(role: str, secret: str) -> str:
        payload = {
            "role": role,
            "iss": "supabase",
            "iat": int(datetime.datetime.utcnow().timestamp()),
            "exp": int((datetime.datetime.utcnow() + datetime.timedelta(days=365*10)).timestamp())
        }
        return jwt.encode(payload, secret, algorithm="HS256")
    
    anon_key = generate_supabase_key("anon", jwt_secret)
    service_role_key = generate_supabase_key("service_role", jwt_secret)
    
    generated_secrets = {
        "DB_PASSWORD": db_password,
        "JWT_SECRET": jwt_secret,
        "SECRET_KEY_BASE": secret_key_base,
        "DB_PORT": str(db_port),
        "REST_PORT": str(rest_port),
        "REALTIME_PORT": str(realtime_port),
        "STORAGE_PORT": str(storage_port),
        "AUTH_PORT": str(auth_port),
        "FUNCTIONS_PORT": str(functions_port),
        "ANON_KEY": anon_key,
        "SERVICE_ROLE_KEY": service_role_key,
        "POSTGRES_DB": "postgres",
        "POSTGRES_USER": "postgres"
    }
    
    # Persist to database
    for key, value in generated_secrets.items():
        db_secret = ProjectSecret(project_id=project_id, key=key, value=value)
        db.add(db_secret)
        
    db.commit()
    return generated_secrets

def reconcile_secrets(db: Session, project_id: str) -> bool:
    """
    Ensures that the secrets in the database are present in the project's .env file.
    Control Plane DB is the Source of Truth.
    Data Plane .env is the Projection.
    """
    # 1. Fetch all secrets for this project from DB
    db_secrets = db.query(ProjectSecret).filter(ProjectSecret.project_id == project_id).all()
    if not db_secrets:
        return False

    # 2. Convert to dictionary
    secrets_map = {s.key: s.value for s in db_secrets}

    # 3. Write to .env file (idempotent, overwrites local with DB truth)
    project_dir = BASE_PROJECTS_DIR / project_id
    project_dir.mkdir(parents=True, exist_ok=True)
    env_file = project_dir / ".env"
    
    env_content = f"# Project: {project_id}\n# Managed by Control Plane\n"
    for key, value in secrets_map.items():
        env_content += f"{key}={value}\n"
    
    env_file.write_text(env_content)
    return True

def import_secrets_from_env(db: Session, project_id: str) -> bool:
    """
    Reverse of reconcile: Imports secrets from .env to DB.
    Used for adopting legacy projects.
    """
    env_path = get_project_env_path(project_id)
    if not env_path.exists():
        return False
        
    local_secrets = dotenv_values(env_path)
    
    # Check what's already in DB to avoid dupes
    existing_secrets = db.query(ProjectSecret).filter(ProjectSecret.project_id == project_id).all()
    existing_keys = {s.key for s in existing_secrets}
    
    for key, value in local_secrets.items():
        if key not in existing_keys:
            db.add(ProjectSecret(project_id=project_id, key=key, value=value))
            
    db.commit()
    return True
