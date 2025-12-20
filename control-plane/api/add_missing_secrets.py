#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from sqlalchemy.orm import Session
from core.database import SessionLocal
from models.project_secret import ProjectSecret
from models.project import Project
import secrets

def add_missing_secrets():
    """Add missing secrets to existing projects"""

    db: Session = SessionLocal()
    try:
        # Get all projects
        projects = db.query(Project).all()

        for project in projects:
            project_id = project.id
            print(f"Checking secrets for project {project_id}")

            # Check what secrets already exist
            existing_secrets = db.query(ProjectSecret).filter(
                ProjectSecret.project_id == project_id
            ).all()

            existing_keys = {secret.key for secret in existing_secrets}
            print(f"  Existing secrets: {existing_keys}")

            # Generate a unique port for this project
            port_suffix = abs(hash(project_id)) % 1000 + 5433
            db_port = str(port_suffix)

            missing_secrets = {}
            if "DB_PORT" not in existing_keys:
                missing_secrets["DB_PORT"] = db_port
            if "REST_PORT" not in existing_keys:
                missing_secrets["REST_PORT"] = str(int(db_port) + 1000)
            if "REALTIME_PORT" not in existing_keys:
                missing_secrets["REALTIME_PORT"] = str(int(db_port) + 2000)

            # Add missing secrets
            for key, value in missing_secrets.items():
                print(f"  Adding {key}: {value}")
                db.add(ProjectSecret(
                    project_id=project_id,
                    key=key,
                    value=value
                ))

        db.commit()
        print("✅ All missing secrets added successfully")

    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_missing_secrets()