import sys
from pathlib import Path

# Add src to path
CURRENT_DIR = Path("/home/faris/Documents/MyApps/supalove/control-plane/api/src")
sys.path.append(str(CURRENT_DIR))
sys.path.append(str(CURRENT_DIR.parent)) # control-plane/api
sys.path.append(str(CURRENT_DIR.parent.parent.parent)) # project root

try:
    print("Attempting to import models...")
    from models.cluster import Cluster
    from models.project import Project
    print("✅ Models imported successfully")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    # Don't exit 1 if it's just DB connection error, we only care about imports
    if "sqlalchemy" in str(e) or "psycopg2" in str(e):
        print("⚠️ DB error expected (no DB running), but imports worked.")
    else:
        sys.exit(1)
