#usage:python3 control-plane/scripts/check_project_status.py <project_id>
import sys
import os

# Add parent dir to path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/api/src")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/api")

from core.database import SessionLocal
from models.project import Project

def check_status(project_id):
    db = SessionLocal()
    try:
        p = db.query(Project).filter(Project.id == project_id).first()
        if p:
            print(f"Project {project_id} status: {p.status}")
        else:
            print(f"Project {project_id} not found in DB")
    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_status(sys.argv[1])
    else:
        # Default or usage
        print("Usage: python3 check_project_status.py <project_id>")
        # check_status("0332bcfcc7cf") # Original default
