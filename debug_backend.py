import sys
import os

# Add src to path
sys.path.append(os.path.join(os.getcwd(), "control-plane/api/src"))

from core.database import SessionLocal
from services.project_service import create_project
from models.project import Project
from models.organization import Organization
from models.subscription import Subscription

db = SessionLocal()
try:
    print("Checking orgs...", file=sys.stderr)
    org = db.query(Organization).first()
    if not org:
        print("No organization found! Cannot create project.", file=sys.stderr)
        sys.exit(1)
    
    org_id = org.id
    print(f"Using Org ID: {org_id}", file=sys.stderr)

    print("Attempting to create project...", file=sys.stderr)
    result = create_project(db, name="debug-proj", org_id=org_id)
    print("Success!", result)

except Exception as e:
    import traceback
    traceback.print_exc()
finally:
    db.close()
