import subprocess
from typing import List, Optional
from services.provisioning_local import BASE_PROJECTS_DIR

def get_project_logs(project_id: str, service_name: str, lines: int = 100) -> str:
    """
    Fetches logs for a specific service in a project using docker compose logs.
    service_name: 'database', 'auth', 'rest', 'realtime', 'storage'
    """
    project_dir = BASE_PROJECTS_DIR / project_id
    if not project_dir.exists():
        return f"Project {project_id} not found"

    # Map friendly service names to docker-compose service names if they differ
    # Assuming standard names: db, auth, rest, realtime, storage, api
    # Check docker-compose.yml or provisioning logic for exact names.
    # Based on standard template:
    # database -> db
    # auth -> auth
    # api -> rest
    # storage -> storage
    # realtime -> realtime
    
    service_map = {
        "database": "db",
        "auth": "auth",
        "api": "rest",
        "rest": "rest",
        "realtime": "realtime",
        "storage": "storage",
        "kong": "kong",
        "meta": "meta"
    }
    
    docker_service = service_map.get(service_name, service_name)
    
    try:
        # Use docker compose logs
        cmd = ["docker", "compose", "logs", "--tail", str(lines), "--no-log-prefix", docker_service]
        
        result = subprocess.run(
            cmd,
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode != 0:
            return f"Error fetching logs: {result.stderr}"
            
        return result.stdout or "(No logs found)"
        
    except subprocess.TimeoutExpired:
        return "Error: Log fetch timed out"
    except Exception as e:
        return f"Error: {str(e)}"
