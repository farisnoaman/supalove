import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).resolve().parent.parent / "control-plane" / "api" / "src"))

from core.database import SessionLocal
from models.project import Project, ProjectPlan
from models.project_secret import ProjectSecret

def fix_shared_secrets():
    db = SessionLocal()
    try:
        shared_projects = db.query(Project).filter(Project.plan == ProjectPlan.shared).all()
        print(f"Found {len(shared_projects)} shared projects.")
        
        count = 0
        for p in shared_projects:
            db_name = f"project_{p.id}"
            db_user = f"{db_name}_user"
            
            # Update or create POSTGRES_DB
            s_db = db.query(ProjectSecret).filter(ProjectSecret.project_id == p.id, ProjectSecret.key == "POSTGRES_DB").first()
            if s_db:
                if s_db.value != db_name:
                    print(f"Updating DB for {p.id}: {s_db.value} -> {db_name}")
                    s_db.value = db_name
                    count += 1
            else:
                print(f"Adding DB for {p.id}: {db_name}")
                db.add(ProjectSecret(project_id=p.id, key="POSTGRES_DB", value=db_name))
                count += 1
                
            # Update or create POSTGRES_USER
            s_user = db.query(ProjectSecret).filter(ProjectSecret.project_id == p.id, ProjectSecret.key == "POSTGRES_USER").first()
            if s_user:
                if s_user.value != db_user:
                    print(f"Updating User for {p.id}: {s_user.value} -> {db_user}")
                    s_user.value = db_user
                    count += 1
            else:
                print(f"Adding User for {p.id}: {db_user}")
                db.add(ProjectSecret(project_id=p.id, key="POSTGRES_USER", value=db_user))
                count += 1
                
        db.commit()
        print(f"Successfully updated {count} secret entries.")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    fix_shared_secrets()
