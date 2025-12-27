import sys
import os

# Add parent dir to path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/api/src")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/api")

from core.database import SessionLocal
from models.project import Project, ProjectStatus
from models.organization import Organization # Ensure registered
from models.subscription import Subscription # Ensure registered
from models.organization_entitlement import OrganizationEntitlement # Ensure registered
from models.cluster import Cluster # Ensure registered
from models.project_secret import ProjectSecret # Ensure registered
from services.project_service import delete_project

def cleanup_all():
    db = SessionLocal()
    try:
        # Get ALL projects, even deleted ones, to ensure we cleanup resources
        projects = db.query(Project).all()
        
        print(f"Found {len(projects)} total projects to verify/cleanup.")
        
        for p in projects:
            print(f"Processing project {p.name} ({p.id}) [Status: {p.status}]...")
            try:
                # Force delete via service (handles container removal)
                delete_project(db, p.id)
                print(f" ✅ Processed {p.id}")
            except Exception as e:
                print(f" ⚠️ Error processing {p.id}: {e}")

        # Usage of services might verify logic, but let's double check filesystem
        import shutil
        from pathlib import Path
        
        # Hardcoded check for data-plane cleanup
        try:
             # Assume we are in control-plane/scripts/
             # Go up to root -> data-plane/projects
             root = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
             projects_dir = root / "data-plane" / "projects"
             
             if projects_dir.exists():
                 print(f"Checking filesystem at {projects_dir}...")
                 count = 0
                 for item in projects_dir.iterdir():
                     if item.is_dir():
                         print(f"Removing leftover directory: {item.name}")
                         try:
                             # Try docker down first just in case
                             os.system(f"cd {item} && docker compose down -v 2>/dev/null")
                             shutil.rmtree(item)
                             count += 1
                         except Exception as e:
                             print(f"Failed to remove {item.name}: {e}")
                 print(f"Filesystem cleanup: Removed {count} orphan directories.")
        except Exception as e:
            print(f"Filesystem cleanup error: {e}")
                
        print("Cleanup complete.")
        
    finally:
        db.close()

if __name__ == "__main__":
    cleanup_all()
