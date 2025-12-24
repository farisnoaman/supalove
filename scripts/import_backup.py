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

def load_env(project_id: str) -> dict:
    """Load environment variables from project .env file."""
    env_path = Path(f"/home/faris/Documents/MyApps/supalove/data-plane/projects/{project_id}/.env")
    env_vars = {}
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    env_vars[key] = value
    return env_vars

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
    
    # Load project environment
    env = load_env(project_id)
    db_user = env.get("POSTGRES_USER", "postgres")
    db_name = env.get("POSTGRES_DB", "postgres")
    
    print(f"🚀 Starting import for project {project_id}...")
    print(f"   Database: {db_name}, User: {db_user}")
    
    # 1. Identify the container
    container_name = f"{project_id}-postgres-1"
    
    print(f"🔍 Checking for container {container_name}...")
    try:
        inspect = subprocess.run(["docker", "inspect", "-f", "{{.State.Running}}", container_name], capture_output=True, text=True)
        if inspect.returncode != 0:
            print(f"❌ Container {container_name} does not exist.")
            sys.exit(1)
        if inspect.stdout.strip() != "true":
            print(f"❌ Container {container_name} is not active. Trying to start it...")
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
    
    # We will pipe the SQL through sed to replace 'postgres' with our actual db_user
    # and to ignore CREATE ROLE errors if possible, but identifying the user is key.
    
    # If it's a gzipped file, we zcat it.
    if is_gzipped:
        # 1. Replace "owner to postgres" with "owner to {db_user}"
        # 2. Ignore "CREATE ROLE" errors is hard in pipe, but fixing owner is critical.
        
        # We construct a command chain:
        # zcat | sed 's/TO postgres/TO {db_user}/g' | psql ...
        
        # Note: We replace "TO postgres" which handles "OWNER TO postgres" and "GRANT ... TO postgres"
        # We also replace "FROM postgres" just in case.
        # Be careful not to replace "postgres" if it's the database name in a connection string, but here it's SQL content.
        
        # Aggressive filtering to ensure data import works even if roles fail
        # 1. Replace postgres -> db_user
        # 2. Comment out CREATE/ALTER/DROP ROLE
        # 3. Comment out CREATE SCHEMA auth (already exists)
        # 4. Comment out GRANT/REVOKE (permission issues)
        # 5. Comment out ALTER DEFAULT PRIVILEGES
        
        filter_cmd = (
            f"sed -E "
            f"'s/TO postgres/TO {db_user}/g; "
            f"s/FROM postgres/FROM {db_user}/g; "
            f"s/^(CREATE|ALTER|DROP) ROLE/-- \\1 ROLE/g; "
            f"s/^(CREATE|ALTER|DROP) SCHEMA auth/-- \\1 SCHEMA auth/g; "
            f"s/^(GRANT|REVOKE) .*/-- \\1 filtered/g; "
            f"s/^ALTER DEFAULT PRIVILEGES/-- ALTER DEFAULT PRIVILEGES/g'"
        )
        
        restore_cmd = f"zcat {dest_path} | {filter_cmd} | psql --username {db_user} --dbname {db_name}"
        docker_cmd = ["docker", "exec", "-i", container_name, "sh", "-c", restore_cmd]
    else:
        # If it's a binary dump (.dump), we can't use sed easily.
        # But assume it's text for now as .pg often is script.
        # If it's custom format, we must use pg_restore.
        # Let's assume text for consistency with the user's issue.
        pass # The user has .gz which is SQL text.

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
        subprocess.run(["docker", "exec", container_name, "rm", dest_path], check=False)
        
        # 4. Restart API to refresh schema cache
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
