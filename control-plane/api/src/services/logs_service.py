import subprocess
from typing import List, Optional
from services.provisioning_local import BASE_PROJECTS_DIR

def get_project_logs(project_id: str, service_name: str, lines: int = 100, is_shared: bool = False) -> str:
    """
    Fetches logs for a specific service in a project.
    For dedicated projects: uses docker compose logs.
    For shared projects: uses docker logs from the shared containers, grepping for project ID if possible.
    """
    service_map = {
        "database": "postgres",
        "auth": "auth",
        "api": "api",
        "rest": "api",
        "functions": "functions",
        "realtime": "realtime",
        "storage": "storage"
    }
    
    docker_service = service_map.get(service_name, service_name)
    
    if is_shared:
        # Shared projects use containers in the supalove_shared stack
        shared_container_map = {
            "postgres": "supalove_shared_postgres",
            "auth": "supalove_shared_auth",
            "api": "supalove_shared_gateway", # The gateway matches project routing
            "realtime": "supalove_shared_realtime",
            "storage": "supalove_shared_storage"
        }
        container_name = shared_container_map.get(docker_service)
        if not container_name:
            return f"Shared logs currently not supported for service: {service_name}"
        
        try:
            # For shared services, we tail the logs. 
            # Ideally we'd grep for the project_id but some services might not include it 
            # in every line. For now, fetch overall logs for the shared service.
            cmd = ["docker", "logs", "--tail", str(lines), container_name]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if result.returncode != 0:
                return f"Error fetching shared logs: {result.stderr}"
            
            # If it's the gateway, we can grep for project_id to show only relevant logs
            if docker_service == "api":
                filtered = [line for line in result.stdout.split('\n') if project_id in line]
                return "\n".join(filtered) or f"(No gateway logs found for project {project_id} in last {lines} lines)"
                
            return result.stdout or "(No logs found)"
        except Exception as e:
            return f"Error: {str(e)}"

    # Dedicated project logic
    project_dir = BASE_PROJECTS_DIR / project_id
    if not project_dir.exists():
        return f"Project directory not found for {project_id}. If this is a shared project, please specify plan."

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
