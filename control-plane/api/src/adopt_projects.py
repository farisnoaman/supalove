
import sys
import os
from pathlib import Path

# Add src to path
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from core.database import SessionLocal
from models.user import User
from models.org_member import OrgMember
from models.project import Project, ProjectStatus
from services.secrets_service import import_secrets_from_env
from services.provisioning_local import BASE_PROJECTS_DIR

def adopt_projects(email: str):
    db = SessionLocal()
    try:
        # 1. Find User and Org
        user = db.query(User).filter(User.email == email).first()
        if not user:
            print(f"User {email} not found.")
            return

        member = db.query(OrgMember).filter(OrgMember.user_id == user.id).first()
        if not member:
            print(f"User {email} is not in any organization.")
            return

        org_id = member.org_id
        print(f"Adopting projects into Organization: {org_id} (User: {email})")

        # 2. Iterate Project Folders
        if not BASE_PROJECTS_DIR.exists():
            print(f"No projects directory found at {BASE_PROJECTS_DIR}")
            return

        adopted_count = 0
        for project_id in os.listdir(BASE_PROJECTS_DIR):
            project_path = BASE_PROJECTS_DIR / project_id
            if not project_path.is_dir() or project_id == "project-template":
                continue

            # Check if exists in DB
            existing_project = db.query(Project).filter(Project.id == project_id).first()
            if existing_project:
                print(f"Skiping {project_id} (already known)")
                continue

            print(f"Found orphaned project: {project_id}")

            # 3. Create Project Record
            # Assume STOPPED unless we check docker state, but safe default
            new_project = Project(
                id=project_id,
                name=f"Legacy {project_id[:6]}",
                org_id=org_id,
                status=ProjectStatus.STOPPED, # User can start it to verify
                created_at=None # Unknown
            )
            db.add(new_project)
            db.commit()

            # 4. Import Secrets
            if import_secrets_from_env(db, project_id):
                print(f"  - Imported secrets from .env")
            else:
                print(f"  - No .env found, secrets might be missing")

            adopted_count += 1
            print(f"  - Adopted successfully!")

        print(f"\nDone. Adopted {adopted_count} projects.")

    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/adopt_projects.py <email>")
        sys.exit(1)
    
    adopt_projects(sys.argv[1])
