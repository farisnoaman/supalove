#!/usr/bin/env python3
"""
Extract and execute SQL from Supabase migration-based backups.
This is for backups from inactive/deleted Supabase projects where re-export isn't possible.
"""

import sys
import re
import gzip
from pathlib import Path
import subprocess

def extract_migration_sql(backup_path: Path) -> list:
    """Extract SQL statements from migration data in backup file."""
    print(f"📖 Reading backup file: {backup_path.name}")
    
    # Read the backup (handle gzip if needed)
    if backup_path.suffix == '.gz':
        with gzip.open(backup_path, 'rt', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    else:
        with open(backup_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    
    print("🔍 Searching for migration data...")
    
    # Look for COPY commands - Supabase stores migrations in table format
    #  Pattern: migration_version TAB {migration SQL in JSON-like format}
    
    migrations = []
    
    # Find all lines that look like migration data (start with a number, have CREATE TABLE)
    lines = content.split('\n')
    for line in lines:
        if 'CREATE TABLE' in line and (line.startswith('20') or '\t{' in line):
            # This looks like a migration line
            # Format: 20250702033122\t{"SQL content"}\temail\t\N
            parts = line.split('\t')
            if len(parts) >= 2:
                try:
                    # The SQL is in the second part, often in a JSON-like string
                    sql_field = parts[1]
                    
                    # Remove surrounding braces if present
                    if sql_field.startswith('{') and sql_field.endswith('}'):
                        sql_field = sql_field[1:-1]
                    
                    # Remove quotes
                    sql_field = sql_field.strip('"')
                    
                    # Unescape the SQL
                    sql = sql_field.replace('\\n', '\n')
                    sql = sql.replace('\\t', '\t')
                    sql = sql.replace('\\"', '"')
                    sql = sql.replace('\\\\', '\\')
                    
                    if len(sql) > 100 and 'CREATE' in sql:  # Basic validation
                        migrations.append(sql)
                        version = parts[0] if parts[0].isdigit() else "unknown"
                        print(f"  ✓ Found migration {version} ({len(sql)} chars)")
                except Exception as e:
                    continue
    
    if not migrations:
        print("❌ No migration data found in backup file.")
        print("\nThis backup might be:")
        print("  1. A standard SQL dump (try normal import)")
        print("  2. In a different format than expected")
        return []
    
    print(f"\n✅ Extracted {len(migrations)} migration(s)")
    return migrations

def execute_sql_in_container(project_id: str, sql: str, db_user: str, db_name: str) -> tuple:
    """Execute SQL in the database container."""
    container_name = f"{project_id}-postgres-1"
    
    # Execute via psql with stdin
    cmd = ["docker", "exec", "-i", container_name, "psql", "-U", db_user, "-d", db_name]
    result = subprocess.run(cmd, input=sql, capture_output=True, text=True)
    
    return result.returncode, result.stdout, result.stderr

def execute_sql_directly(sql: str, db_user: str, db_name: str, host: str, port: int, password: str) -> tuple:
    """Execute SQL directly via psycopg2 (for shared projects)."""
    import psycopg2
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=db_user,
            password=password,
            dbname=db_name
        )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.close()
        return 0, "Success", ""
    except Exception as e:
        return 1, "", str(e)

def execute_migrations(project_id: str, migrations: list, db_user: str, db_name: str, is_shared: bool = False, shared_creds: dict = None):
    """Execute extracted migrations against project database."""
    target = "shared cluster" if is_shared else f"container {project_id}-postgres-1"
    
    print(f"\n🚀 Executing {len(migrations)} migration(s) on {target}...")
    print(f"   Database: {db_name}, User: {db_user}\n")
    
    success_count = 0
    error_count = 0
    
    for idx, sql in enumerate(migrations, 1):
        print(f"[{idx}/{len(migrations)}] Executing migration...", end=" ", flush=True)
        
        if is_shared:
            returncode, stdout, stderr = execute_sql_directly(
                sql, db_user, db_name, 
                shared_creds['host'], shared_creds['port'], shared_creds['password']
            )
        else:
            returncode, stdout, stderr = execute_sql_in_container(project_id, sql, db_user, db_name)
        
        if returncode == 0:
            print("✅ OK")
            success_count += 1
        else:
            # Check if errors are benign (already exists)
            real_errors = [line for line in stderr.split('\n') 
                          if 'ERROR:' in line 
                          and 'already exists' not in line
                          and 'does not exist, skipping' not in line]
            
            if real_errors:
                print("❌ FAILED")
                for error in real_errors[:2]:
                    print(f"    {error}")
                error_count += 1
            else:
                print("✅ OK (with warnings)")
                success_count += 1
    
    print(f"\n📊 Summary: {success_count} successful, {error_count} with errors")
    if error_count > 0:
        print("\n❌ Migration process completed with critical errors.")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 extract_from_migrations.py <project_id> <backup_file>")
        print("\nThis tool extracts SQL from Supabase migration-based backups.")
        print("Use this when you have a backup from an inactive/deleted Supabase project.")
        sys.exit(1)
    
    project_id = sys.argv[1]
    backup_path = Path(sys.argv[2])
    
    if not backup_path.exists():
        print(f"❌ Backup file not found: {backup_path}")
        sys.exit(1)
    
    # Load project env to get DB credentials
    project_dir = Path(f"/home/faris/Documents/MyApps/supalove/data-plane/projects/{project_id}")
    env_path = project_dir / ".env"
    db_user = "postgres"
    db_name = "postgres"
    is_shared = not project_dir.exists()
    shared_creds = {}
    
    if not is_shared:
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    if line.startswith("POSTGRES_USER="):
                        db_user = line.split("=", 1)[1].strip()
                    elif line.startswith("POSTGRES_DB="):
                        db_name = line.split("=", 1)[1].strip()
    else:
        # For shared projects, we assume the naming convention and shared cluster info
        # In a real scenario, we might want to pass these as arguments or env vars
        import os
        db_name = f"project_{project_id}"
        db_user = f"{db_name}_user"
        shared_creds = {
            'host': os.getenv("SHARED_POSTGRES_HOST", "localhost"),
            'port': int(os.getenv("SHARED_POSTGRES_PORT", "5434")),
            'password': os.getenv("SHARED_POSTGRES_PASSWORD", "postgres")
        }
    
    print(f"🎯 Target Project: {project_id} ({'Shared' if is_shared else 'Dedicated'})")
    print(f"   Database: {db_name}, User: {db_user}\n")
    
    # Extract migrations
    migrations = extract_migration_sql(backup_path)
    
    if not migrations:
        sys.exit(1)
    
    # Execute migrations
    execute_migrations(project_id, migrations, db_user, db_name, is_shared, shared_creds)
    
    print("\n✨ Migration extraction complete!")
    if not is_shared:
        print(f"   Run: docker exec -i {project_id}-postgres-1 psql -U {db_user} -d {db_name} -c \"\\dt public.*\"")
    else:
        print(f"   Imports applied to shared database {db_name}.")
    print("   to verify tables were created.")

if __name__ == "__main__":
    main()
