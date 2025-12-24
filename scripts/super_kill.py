import subprocess
import os
import signal
import sys

def get_stuck_containers():
    print("Finding stuck Supalove containers...")
    cmd = ["docker", "ps", "-a", "--format", "{{.Names}}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    targets = []
    # Filter for our specific project containers
    keywords = ["supalove", "gateway-1", "storage-1", "functions-1", "auth-1", "realtime-1", "api-1", "postgres-1"]
    
    for line in result.stdout.strip().split('\n'):
        name = line.strip()
        if not name: continue
        
        # Check if it matches our patterns
        if any(k in name for k in keywords):
            targets.append(name)
            
    return targets

def kill_and_remove(container_name):
    # 1. Get PID
    inspect_cmd = ["docker", "inspect", "--format", "{{.State.Pid}}", container_name]
    res = subprocess.run(inspect_cmd, capture_output=True, text=True)
    
    pid_str = res.stdout.strip()
    if not pid_str or pid_str == "0":
        print(f"[{container_name}] No PID found (already dead?). Trying rm...")
    else:
        try:
            pid = int(pid_str)
            print(f"[{container_name}] Found PID {pid}. Killing...")
            os.kill(pid, signal.SIGKILL)
            print(f"[{container_name}] \033[92mKilled PID {pid}\033[0m")
        except ProcessLookupError:
            print(f"[{container_name}] PID {pid} not found (already gone).")
        except PermissionError:
            print(f"[{container_name}] \033[91mPermission denied killing PID {pid}\033[0m")
        except Exception as e:
            print(f"[{container_name}] Error killing PID: {e}")

    # 2. Docker RM
    print(f"[{container_name}] Removing from docker...")
    subprocess.run(["docker", "rm", "-f", container_name], capture_output=True)

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("\033[91mCRITICAL: This script MUST be run as root (sudo).\033[0m")
        sys.exit(1)
        
    targets = get_stuck_containers()
    if not targets:
        print("No Supalove containers found!")
        sys.exit(0)
        
    print(f"Found {len(targets)} containers to handle.")
    
    for container in targets:
        kill_and_remove(container)
        
    print("\n✅ Super Kill complete. Run 'docker ps' to verify.")
