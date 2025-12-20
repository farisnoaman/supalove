## Example usage:
#./control-plane/api/.venv/bin/python3 check_minio.py
#./control-plane/api/.venv/bin/python3 check_auth.py 29315029c9e7
###########
import sys
import os
from pathlib import Path

# Setup paths to import AuthService from the control plane
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT / "control-plane" / "api" / "src"))

try:
    from services.auth_service import AuthService
except ImportError:
    print("Error: Could not import AuthService. Make sure the path is correct.")
    sys.exit(1)

def check_auth(project_id):
    # Set necessary environment variables for AuthService if not already set
    os.environ.setdefault("KEYCLOAK_URL", "http://localhost:8080")
    os.environ.setdefault("KEYCLOAK_ADMIN", "admin")
    os.environ.setdefault("KEYCLOAK_ADMIN_PASSWORD", "admin")

    auth = AuthService()
    try:
        users = auth.list_users(project_id)
        print(f"--- Users for project: {project_id} ---")
        if not users:
            print("No users found.")
        for u in users:
            print(f"Email: {u.get('email', 'N/A')}")
            print(f"ID:    {u.get('id')}")
            print(f"Status: {'Enabled' if u.get('enabled') else 'Disabled'}")
            print("-" * 30)
    except Exception as e:
        print(f"Error listing users: {e}")

if __name__ == "__main__":
    target_id = "29315029c9e7" # Default test project
    if len(sys.argv) > 1:
        target_id = sys.argv[1]
    
    check_auth(target_id)
