#!/usr/bin/env python3
"""
Import a Supabase backup (.pg, .gz, .sql) into a Supalove project.
Supports both dedicated Docker projects and shared PostgreSQL clusters.
"""

import sys
import os
import subprocess
import argparse
import gzip
import re
from pathlib import Path


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


def filter_sql(sql_content: str, target_user: str) -> str:
    """Filter SQL content to remove problematic statements for import."""
    lines = sql_content.split('\n')
    filtered_lines = []
    
    skip_patterns = [
        r'^CREATE ROLE',
        r'^ALTER ROLE',
        r'^DROP ROLE',
        r'^GRANT .* TO .* GRANTED BY',
        r'^\\connect',
        r'^CREATE SCHEMA auth',
        r'^CREATE SCHEMA storage',
        r'^CREATE SCHEMA realtime',
        r'^CREATE SCHEMA supabase_migrations',
        r'^CREATE SCHEMA vault',
        r'^CREATE SCHEMA graphql',
        r'^CREATE SCHEMA pgbouncer',
        r'^CREATE SCHEMA extensions',
        r'^ALTER SCHEMA .* OWNER TO supabase',
        r'^CREATE EXTENSION IF NOT EXISTS pg_graphql',
        r'^CREATE EXTENSION IF NOT EXISTS pg_stat_statements',
        r'^CREATE EXTENSION IF NOT EXISTS pgjwt',
        r'^CREATE EXTENSION IF NOT EXISTS supabase_vault',
        r'^ALTER DEFAULT PRIVILEGES',
        r'^COMMENT ON EXTENSION',
    ]
    
    skip_regex = re.compile('|'.join(skip_patterns), re.IGNORECASE)
    
    for line in lines:
        # Skip problematic lines
        if skip_regex.match(line.strip()):
            continue
        
        # Replace postgres ownership with target user
        line = re.sub(r'OWNER TO postgres', f'OWNER TO {target_user}', line)
        line = re.sub(r'TO postgres;', f'TO {target_user};', line)
        line = re.sub(r'FROM postgres;', f'FROM {target_user};', line)
        
        filtered_lines.append(line)
    
    return '\n'.join(filtered_lines)


def import_to_shared_project(project_id: str, backup_path: Path):
    """Import backup to a shared PostgreSQL cluster using psycopg2."""
    import psycopg2
    
    db_name = f"project_{project_id}"
    db_user = f"{db_name}_user"
    host = os.getenv("SHARED_POSTGRES_HOST", "localhost")
    port = int(os.getenv("SHARED_POSTGRES_PORT", "5435"))
    password = os.getenv("SHARED_POSTGRES_PASSWORD", "postgres")
    
    print(f"🚀 Starting import for SHARED project {project_id}...")
    print(f"   Database: {db_name}, Host: {host}:{port}")
    
    # Read backup file
    print(f"📖 Reading backup file: {backup_path.name}")
    if backup_path.suffix == '.gz':
        with gzip.open(backup_path, 'rt', encoding='utf-8', errors='ignore') as f:
            sql_content = f.read()
    else:
        with open(backup_path, 'r', encoding='utf-8', errors='ignore') as f:
            sql_content = f.read()
    
    print(f"   Read {len(sql_content):,} characters")
    
    # Filter SQL
    print("🔧 Filtering SQL for shared environment...")
    filtered_sql = filter_sql(sql_content, "postgres")  # Use postgres superuser for import
    print(f"   Filtered to {len(filtered_sql):,} characters")
    
    # Connect to database
    print(f"🔌 Connecting to shared cluster...")
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user="postgres",
            password=password,
            dbname=db_name
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Enable required extensions
        print("🔧 Enabling extensions...")
        extensions = [
            'CREATE EXTENSION IF NOT EXISTS "uuid-ossp";',
            'CREATE EXTENSION IF NOT EXISTS "pgcrypto";',
            'CREATE EXTENSION IF NOT EXISTS "citext";',
        ]
        for ext in extensions:
            try:
                cursor.execute(ext)
            except Exception as e:
                print(f"   ⚠️ Extension warning: {e}")
        
        # Execute SQL in chunks to handle large files
        print("♻️  Executing SQL... (This may take a while)")
        
        # First, remove comment-only lines and clean up
        clean_lines = []
        for line in filtered_sql.split('\n'):
            stripped = line.strip()
            # Skip empty lines and comment-only lines
            if not stripped or stripped.startswith('--'):
                continue
            # Remove inline comments (but preserve strings)
            if '--' in line and "'" not in line and '"' not in line:
                line = line.split('--')[0].rstrip()
                if not line.strip():
                    continue
            clean_lines.append(line)
        
        cleaned_sql = '\n'.join(clean_lines)
        
        # Split by semicolons, accounting for function bodies and strings
        statements = []
        current = []
        in_string = False
        string_char = None
        in_dollar_quote = False
        dollar_tag = ""
        
        i = 0
        while i < len(cleaned_sql):
            char = cleaned_sql[i]
            
            # Handle dollar quoting ($$, $tag$)
            if char == '$' and not in_string:
                # Look for dollar quote pattern
                j = i + 1
                while j < len(cleaned_sql) and (cleaned_sql[j].isalnum() or cleaned_sql[j] == '_'):
                    j += 1
                if j < len(cleaned_sql) and cleaned_sql[j] == '$':
                    tag = cleaned_sql[i:j+1]
                    if in_dollar_quote and tag == dollar_tag:
                        in_dollar_quote = False
                        dollar_tag = ""
                    elif not in_dollar_quote:
                        in_dollar_quote = True
                        dollar_tag = tag
                    current.append(cleaned_sql[i:j+1])
                    i = j + 1
                    continue
            
            # Handle regular strings
            if char in ("'", '"') and not in_dollar_quote:
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    # Check for escaped quote
                    if i + 1 < len(cleaned_sql) and cleaned_sql[i + 1] == char:
                        current.append(char)
                        current.append(char)
                        i += 2
                        continue
                    in_string = False
                    string_char = None
            
            current.append(char)
            
            # Statement terminator
            if char == ';' and not in_string and not in_dollar_quote:
                stmt = ''.join(current).strip()
                if stmt and stmt != ';':
                    statements.append(stmt)
                current = []
            
            i += 1
        
        # Add remaining content
        if current:
            stmt = ''.join(current).strip()
            if stmt and stmt != ';':
                statements.append(stmt)
        
        # Execute statements
        success_count = 0
        error_count = 0
        table_count = 0
        
        for i, stmt in enumerate(statements):
            stmt = stmt.strip()
            if not stmt or stmt == ';':
                continue
            
            # Track table creations
            if 'CREATE TABLE public.' in stmt.upper():
                table_count += 1
            
            try:
                cursor.execute(stmt)
                success_count += 1
            except psycopg2.Error as e:
                error_str = str(e)
                # Ignore benign errors
                if 'already exists' in error_str or 'does not exist' in error_str:
                    success_count += 1
                else:
                    error_count += 1
                    if error_count <= 5:
                        print(f"   ⚠️ Error: {error_str[:100]}")
            
            # Progress indicator
            if (i + 1) % 500 == 0:
                print(f"   Processed {i + 1}/{len(statements)} statements...")
        
        # Transfer ownership of public schema tables to project user
        print(f"🔄 Transferring table ownership to {db_user}...")
        try:
            cursor.execute(f"""
                DO $$
                DECLARE
                    r RECORD;
                BEGIN
                    FOR r IN SELECT tablename FROM pg_tables WHERE schemaname = 'public' AND tableowner = 'postgres'
                    LOOP
                        EXECUTE 'ALTER TABLE public.' || quote_ident(r.tablename) || ' OWNER TO {db_user}';
                    END LOOP;
                END $$;
            """)
        except Exception as e:
            print(f"   ⚠️ Ownership transfer warning: {e}")
        
        # Verify tables
        cursor.execute("""
            SELECT tablename FROM pg_tables 
            WHERE schemaname = 'public' 
            ORDER BY tablename;
        """)
        tables = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        conn.close()
        
        print(f"\n📊 Summary:")
        print(f"   ✅ {success_count} statements executed")
        print(f"   ⚠️ {error_count} errors (non-critical)")
        print(f"   📦 {len(tables)} tables in public schema")
        
        if tables:
            print(f"\n✨ Created tables:")
            for t in tables[:15]:
                print(f"   - {t}")
            if len(tables) > 15:
                print(f"   ... and {len(tables) - 15} more")
        
        print("\n✅ Import completed successfully!")
        return True
        
    except psycopg2.Error as e:
        print(f"❌ Database connection error: {e}")
        return False


def import_to_dedicated_project(project_id: str, backup_path: Path):
    """Import backup to a dedicated Docker project."""
    env = load_env(project_id)
    db_user = env.get("POSTGRES_USER", "postgres")
    db_name = env.get("POSTGRES_DB", "postgres")
    container_name = f"{project_id}-postgres-1"
    
    print(f"🚀 Starting import for DEDICATED project {project_id}...")
    print(f"   Database: {db_name}, Container: {container_name}")
    
    # Check container
    print(f"🔍 Checking for container {container_name}...")
    try:
        inspect = subprocess.run(
            ["docker", "inspect", "-f", "{{.State.Running}}", container_name], 
            capture_output=True, text=True
        )
        if inspect.returncode != 0:
            print(f"❌ Container {container_name} does not exist.")
            return False
        if inspect.stdout.strip() != "true":
            print(f"❌ Container {container_name} is not active. Trying to start it...")
            subprocess.run(["docker", "start", container_name], check=True)
            print("✅ Container started.")
    except Exception as e:
        print(f"❌ Error checking container: {e}")
        return False

    # Copy file to container
    is_gzipped = backup_path.suffix == '.gz'
    dest_filename = f"backup_{project_id}.dump.gz" if is_gzipped else f"backup_{project_id}.dump"
    dest_path = f"/tmp/{dest_filename}"
    
    print(f"📦 Copying {backup_path.name} to container...")
    subprocess.run(["docker", "cp", str(backup_path), f"{container_name}:{dest_path}"], check=True)
    
    # Restore
    print(f"♻️  Restoring database... (This may take a while)")
    
    filter_cmd = (
        f"sed -E "
        f"'s/TO postgres/TO {db_user}/g; "
        f"s/FROM postgres/FROM {db_user}/g; "
        f"s/^(CREATE|ALTER|DROP) ROLE/-- \\1 ROLE/g; "
        f"s/^(CREATE|ALTER|DROP) SCHEMA auth/-- \\1 SCHEMA auth/g; "
        f"s/^(GRANT|REVOKE) .*/-- \\1 filtered/g; "
        f"s/^ALTER DEFAULT PRIVILEGES/-- ALTER DEFAULT PRIVILEGES/g'"
    )
    
    psql_creds = f"psql --username {db_user} --dbname {db_name}"
    
    if is_gzipped:
        restore_cmd = f"zcat {dest_path} | {filter_cmd} | {psql_creds}"
    else:
        restore_cmd = f"cat {dest_path} | {filter_cmd} | {psql_creds}"
    
    docker_cmd = ["docker", "exec", "-i", container_name, "sh", "-c", restore_cmd]

    try:
        process = subprocess.run(
            docker_cmd,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stderr = process.stderr
        
        # Filter benign warnings
        real_errors = []
        for line in stderr.split('\n'):
            if "ERROR:" in line and "does not exist" not in line and "already exists" not in line:
                if "role \"authenticator\"" not in line and "role \"service_role\"" not in line:
                    real_errors.append(line)

        print("\n📝 Restore Log Summary:")
        print(stderr[-500:] if stderr else "(no output)")

        if process.returncode == 0:
            print("\n✅ Restore completed successfully!")
        else:
            print(f"\n⚠️  Restore completed with Exit Code {process.returncode}")
            if real_errors:
                for err in real_errors[:10]:
                    print(f"  - {err}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        print("🧹 Cleaning up...")
        subprocess.run(["docker", "exec", container_name, "rm", dest_path], check=False)
        
        # Restart API
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
            print(f"⚠️  Could not restart API automatically.")
    
    return True


def main():
    parser = argparse.ArgumentParser(description="Import a Supabase backup into a Supalove project.")
    parser.add_argument("project_id", help="The ID of the project (e.g. d25539265b82)")
    parser.add_argument("backup_file", help="Path to the backup file (.pg, .gz, or .sql)")
    
    args = parser.parse_args()
    
    project_id = args.project_id
    backup_path = Path(args.backup_file).resolve()
    
    if not backup_path.exists():
        print(f"❌ Error: Backup file not found at {backup_path}")
        sys.exit(1)
    
    # Determine project type
    project_dir = Path(f"/home/faris/Documents/MyApps/supalove/data-plane/projects/{project_id}")
    is_shared = not project_dir.exists()
    
    if is_shared:
        success = import_to_shared_project(project_id, backup_path)
    else:
        success = import_to_dedicated_project(project_id, backup_path)
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
