import os
import shutil
import subprocess
import re
from pathlib import Path

def force_stop_containers():
    print("SEARCHING for Supalove containers to force stop...")
    
    # 1. Get all container names
    result = subprocess.run(["docker", "ps", "-a", "--format", "{{.Names}}"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error getting docker containers")
        return

    all_containers = result.stdout.strip().split('\n')
    
    # 2. Filter for project containers and control plane
    # Patterns: 
    # - {hex_id}-{service}-1 (e.g. ac22d1b05112-gateway-1)
    # - supalove-*
    # - project_{id}_db
    
    targets = []
    project_pattern = re.compile(r'^[a-f0-9]{12}-(gateway|storage|functions|auth|realtime|api|postgres)-1$')
    
    for name in all_containers:
        if not name: continue
        
        is_target = False
        if name.startswith("supalove"):
            is_target = True
        elif project_pattern.match(name):
            is_target = True
        elif "_project_" in name or name.startswith("project_"): # Some legacy naming?
            is_target = True
            
        if is_target:
            targets.append(name)

    if not targets:
        print("No containers found to stop.")
    else:
        print(f"Found {len(targets)} containers to remove.")
        # batch remove
        cmd = ["docker", "rm", "-f"] + targets
        subprocess.run(cmd, check=False)
        print("Containers removed.")

def nuke_directories():
    root_dir = Path(__file__).resolve().parent.parent
    projects_dir = root_dir / "data-plane" / "projects"
    
    if not projects_dir.exists():
        return

    print(f"Cleaning artifacts in {projects_dir}...")
    
    # Try to fix permissions before deleting
    # We can't use sudo, but we can try to be owner if we created them
    # If they were created by root inside docker and volume mounted... we might have issues.
    # We will try 'chmod -R 777' on the dir if possible.
    
    try:
        subprocess.run(["chmod", "-R", "777", str(projects_dir)], check=False)
    except:
        pass

    for item in projects_dir.iterdir():
        if item.is_dir():
            print(f"  - Removing {item.name}")
            try:
                shutil.rmtree(item)
            except Exception as e:
                print(f"    ! Standard delete failed: {e}")
                print("    Trying force rm...")
                subprocess.run(["rm", "-rf", str(item)], check=False)

    print("Directory cleanup finished.")

def nuke_volumes():
    # Prune unnamed volumes which might be left over
    print("Pruning docker volumes...")
    subprocess.run(["docker", "volume", "prune", "-f"], check=False)
    
    # Also explicitly remove specific named volumes involved
    # supalove_control_plane_data, etc.
    subprocess.run(["docker", "volume", "rm", "supalove_control_plane_data", "supalove_minio_data", "supalove_prometheus_data", "supalove_grafana_data", "supalove_loki_data"], check=False, stderr=subprocess.DEVNULL)
    
if __name__ == "__main__":
    print("☢️  STARTING AGGRESSIVE CLEANUP ☢️")
    force_stop_containers()
    nuke_directories()
    nuke_volumes()
    print("\n✅ Reset complete.")
