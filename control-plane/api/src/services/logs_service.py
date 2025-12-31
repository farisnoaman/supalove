import subprocess
from typing import List, Optional
from services.provisioning_local import BASE_PROJECTS_DIR

def _find_shared_container(service_pattern: str) -> Optional[str]:
    """
    Dynamically find the running shared container name by pattern.
    Returns the container name or None if not found.
    """
    try:
        cmd = ["docker", "ps", "--filter", f"name={service_pattern}", "--format", "{{.Names}}"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if result.returncode == 0 and result.stdout.strip():
            # Return the first matching container (most recent if multiple)
            containers = result.stdout.strip().split('\n')
            return containers[0] if containers else None
    except Exception:
        pass
    return None

def get_project_logs(project_id: str, service_name: str, lines: int = 100, is_shared: bool = False) -> str:
    """
    Fetches logs for a specific service in a project.
    For dedicated projects: uses docker compose logs.
    For shared projects: uses docker logs from the shared containers, with filtering where possible.
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
        # Dynamically find the actual running container names
        shared_container_patterns = {
            "postgres": "supalove_shared_postgres",
            "auth": "supalove_shared_auth",
            "api": "supalove_shared_gateway",  # Gateway handles API routing
            "realtime": "supalove_shared_realtime",
            "storage": "supalove_shared_storage"
        }
        
        pattern = shared_container_patterns.get(docker_service)
        if not pattern:
            return f"Logs not supported for service: {service_name}"
        
        # Find the actual running container
        container_name = _find_shared_container(pattern)
        if not container_name:
            return f"Shared {service_name} container not found or not running"
        
        try:
            # Fetch logs from the shared container
            cmd = ["docker", "logs", "--tail", str(lines), container_name]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if result.returncode != 0:
                return f"Error fetching logs: {result.stderr}"
            
            all_logs = result.stdout + result.stderr  # Combine stdout and stderr
            
            # Apply service-specific filtering
            if docker_service == "postgres":
                # Filter PostgreSQL logs by database name
                db_name = f"project_{project_id}"
                filtered = [line for line in all_logs.split('\n') if db_name in line]
                if filtered:
                    return "\n".join(filtered)
                else:
                    return f"(No database logs found for {db_name} in last {lines} lines)\n\nNote: PostgreSQL logs are filtered by database name."
            
            elif docker_service == "api":
                # Filter gateway logs by project ID
                filtered = [line for line in all_logs.split('\n') if project_id in line]
                if filtered:
                    return "\n".join(filtered)
                else:
                    return f"(No gateway logs found for project {project_id} in last {lines} lines)\n\nNote: Gateway logs are filtered by project ID in request paths."
            
            else:
                # For auth, realtime, storage - these are multi-tenant services
                # We can't easily filter by project, so show a warning
                warning = f"⚠️  Note: {service_name.upper()} is a shared multi-tenant service.\n"
                warning += f"Logs below may include activity from ALL projects, not just {project_id}.\n"
                warning += "=" * 80 + "\n\n"
                return warning + (all_logs or "(No logs found)")
                
        except subprocess.TimeoutExpired:
            return f"Error: Log fetch timed out for {container_name}"
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
