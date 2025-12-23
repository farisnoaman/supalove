import sys
import os
import subprocess
import argparse
from pathlib import Path

def run_command(cmd, shell=False):
    """Run a shell command and return output."""
    try:
        result = subprocess.run(
            cmd, 
            shell=shell, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Import a Supabase .pg backup into a Supalove project.")
    parser.add_argument("project_id", help="The ID of the project (e.g. d25539265b82)")
    parser.add_argument("backup_file", help="Path to the .pg backup file")
    
    args = parser.parse_args()
    
    project_id = args.project_id
    backup_path = Path(args.backup_file).resolve()
    
    if not backup_path.exists():
        print(f"Error: Backup file not found at {backup_path}")
        sys.exit(1)
        
    print(f"🚀 Starting import for project {project_id}...")
    
    # 1. Identify the container
    container_name = f"{project_id}-postgres-1"
    
    print(f"🔍 Checking for container {container_name}...")
    try:
        inspect = subprocess.run(["docker", "inspect", "-f", "{{.State.Running}}", container_name], capture_output=True, text=True)
        if inspect.returncode != 0:
            print(f"❌ Container {container_name} does not exist.")
            sys.exit(1)
        if inspect.stdout.strip() != "true":
            print(f"❌ Container {container_name} is running but not active (State=false). Trying to start it...")
            run_command(["docker", "start", container_name])
            print("✅ Container started.")
    except Exception as e:
        print(f"❌ Error checking container: {e}")
        sys.exit(1)

    # 2. Copy the file to the container
    is_gzipped = backup_path.suffix == '.gz'
    dest_filename = "backup.dump.gz" if is_gzipped else "backup.dump"
    dest_path = f"/tmp/{dest_filename}"
    
    print(f"📦 Copying {backup_path.name} to container...")
    run_command(["docker", "cp", str(backup_path), f"{container_name}:{dest_path}"])
    
    # 3. Restore strategy
    print(f"♻️  Restoring database... (This may take a while)")
    
    # If gzipped, we need to zcat it into psql OR if it's a custom dump, use pg_restore.
    # Supabase .gz backups (via 'Download') are usually SQL text compressed.
    # .pg backups are Custom Format (pg_restore).
    
    # We'll try to determine type.
    if is_gzipped:
        # Assuming SQL text compressed with gzip
        # We use zcat inside the container to pipe to psql
        restore_cmd = f"zcat {dest_path} | psql --username postgres --dbname postgres"
        docker_cmd = ["docker", "exec", "-i", container_name, "sh", "-c", restore_cmd]
    else:
        # Standard pg_restore for .pg, .dump
        docker_cmd = [
            "docker", "exec", "-i", container_name,
            "pg_restore",
            "--username", "postgres",
            "--dbname", "postgres",
            "--clean",
            "--if-exists",
            "--no-owner",
            "--role=postgres",
            "--verbose",
            dest_path
        ]

    try:
        process = subprocess.run(
            docker_cmd,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Analyze result
        stderr = process.stderr
        
        # Filter benign warnings
        real_errors = []
        for line in stderr.split('\n'):
            if "ERROR:" in line and "does not exist" not in line and "already exists" not in line:
                 if "role \"authenticator\"" not in line and "role \"service_role\"" not in line:
                     real_errors.append(line)

        print("\n📝 Restore Log Summary:")
        print(stderr[-500:])

        if process.returncode == 0:
            print("\n✅ Restore completed successfully!")
        else:
            print(f"\n⚠️  Restore completed with Exit Code {process.returncode}")
            if real_errors:
                for err in real_errors[:10]:
                    print(f"  - {err}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        print("🧹 Cleaning up...")
        run_command(["docker", "exec", container_name, "rm", dest_path])
        
        # 4. Restart API to refresh schema cache (use docker compose for better permissions handling)
        project_dir = Path(f"/home/faris/Documents/MyApps/supalove/data-plane/projects/{project_id}")
        print(f"🔄 Restarting API service to refresh schema cache...")
        try:
            subprocess.run(
                ["docker", "compose", "restart", "api"],
                cwd=project_dir,
                check=True,
                capture_output=True
            )
            print("✅ API restarted. Your tables should now be visible.")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Could not restart API automatically: {e.stderr.decode() if e.stderr else 'Unknown error'}")
            print(f"    Run manually: docker compose -f {project_dir}/docker-compose.yml restart api")

if __name__ == "__main__":
    main()
