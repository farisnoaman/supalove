import sys
import os

# Add src to path
sys.path.append(os.path.join(os.getcwd(), "control-plane/api/src"))

from core.database import SessionLocal
from services.project_service import create_project
from models.project import Project

db = SessionLocal()
try:
    print("Checking orgs...", file=sys.stderr)
    # We cheat and pass None as org_id if allowed, or pick a random string?
    # Schema likely enforces it.
    # Let's see if we can find an org.
    # Actually, let's just use a dummy UUID if FK constraints aren't strict, or fetch one.
    # Assuming FK is strict.
    # from models.organization import Organization
    # org = db.query(Organization).first()
    # if org:
    #     org_id = org.id
    # else:
    #     print("No org found, using dummy")
    #     org_id = "org_dummy"
    
    # Actually, let's try to query an org first.
    # To avoid importing too many models, I'll valid org_id from previous output?
    # No, I'll just try to Create. logic in usage_service might fail if org not found.
    
    print("Attempting to create project...", file=sys.stderr)
    # We use a hardcoded org_id known to exist or fetched via SQL?
    # Let's try with a dummy first, risk of IntegrityError.
    
    # Better: Fetch org using raw SQL to be safe?
    # Or just use the model if I can import it.
    # I don't know where Organization model is. 'models.organization'? 
    
    # Let's try to create with org_id='test-org' and see if it fails with invalid org or something else.
    result = create_project(db, name="debug-proj", org_id="test-org")
    print("Success!", result)

except Exception as e:
    import traceback
    traceback.print_exc()
finally:
    db.close()
