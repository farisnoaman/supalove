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
    
    # Look for migration data patterns:
    # 1. 14-digit timestamp followed by tab and SQL: 20250702033122\tSQL...
    # 2. Lines containing tab and curly braces around SQL: ...\t{SQL...}
    
    migrations = []
    lines = content.split('\n')
    
    # Pattern for 14-digit timestamp versioning
    version_pattern = re.compile(r'^(\d{14})\t')
    
    for line in lines:
        # Check if line looks like a migration record
        is_migration = False
        parts = []
        
        if version_pattern.match(line):
            is_migration = True
            parts = line.split('\t')
        elif '\t{' in line and '}' in line:
            # Maybe not starting with timestamp but has the {SQL} structure
            is_migration = True
            parts = line.split('\t')
            
        if is_migration and len(parts) >= 2:
            try:
                # Find the field that contains SQL (usually field 2 or 3)
                # We'll look for fields containing common SQL keywords
                for sql_candidate in parts[1:]:
                    sql_candidate = sql_candidate.strip()
                    
                    # Unpack if it's in {SQL} format
                    if sql_candidate.startswith('{') and sql_candidate.endswith('}'):
                        sql_candidate = sql_candidate[1:-1]
                    
                    # Remove quotes if present
                    if (sql_candidate.startswith('"') and sql_candidate.endswith('"')) or \
                       (sql_candidate.startswith("'") and sql_candidate.endswith("'")):
                        sql_candidate = sql_candidate[1:-1]
                    
                    # Unescape the SQL
                    sql = sql_candidate.replace('\\n', '\n')
                    sql = sql.replace('\\t', '\t')
                    sql = sql.replace('\\"', '"')
                    sql = sql.replace('\\\'', '\'')
                    sql = sql.replace('\\\\', '\\')
                    
                    # Fix: Strip leading "comment-style" labels often found in Supabase backups
                    # e.g. "-- my_table CREATE TABLE ..." -> "CREATE TABLE ..."
                    sql_stripped = sql.strip()
                    if sql_stripped.startswith("--"):
                        # Find the first occurrence of a major keyword
                        keywords_pattern = re.compile(r'(CREATE|ALTER|INSERT|UPDATE|DELETE|DROP|GRANT|REVOKE)\s', re.IGNORECASE)
                        match = keywords_pattern.search(sql_stripped)
                        if match:
                            # Keep everything from the keyword onwards
                            sql = sql_stripped[match.start():]
                            print(f"    - Stripped comment prefix, new start: {sql[:30]}...")

                    # Refined validation: must contain at least one characteristic SQL keyword
                    sql_clean = sql.upper()
                    keywords = ['CREATE ', 'ALTER ', 'INSERT ', 'UPDATE ', 'DELETE ', 'DROP ', 'GRANT ', 'REVOKE ']
                    if any(kw in sql_clean for kw in keywords) and len(sql) > 5:
                        migrations.append(sql)
                        version = parts[0] if parts[0].isdigit() else "unknown"
                        print(f"  ✓ Found migration {version} ({len(sql)} chars)")
                        break # Found SQL for this migration record
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
    
    # Pre-process migrations to ensure ownership and search path
    processed_migrations = []
    for sql in migrations:
        # Replace postgres owner with project user
        sql = sql.replace("TO postgres", f"TO {db_user}")
        sql = sql.replace("OWNER TO postgres", f"OWNER TO {db_user}")
        
        # Ensure we are operating on the public schema if not specified
        if "SET search_path" not in sql:
            sql = f"SET search_path TO public, auth, storage, extensions;\n{sql}"
            
        processed_migrations.append(sql)
    
    for idx, sql in enumerate(processed_migrations, 1):
        print(f"[{idx}/{len(processed_migrations)}] Executing migration...", end=" ", flush=True)
        
        if is_shared:
            # For shared projects, we use the postgres superuser to execute the migration
            # but getting the connection right.
            # We already replaced ownership in the SQL, so running as postgres is fine.
            
            # First, ensure extensions exist
            if idx == 1:
                print(f"   Ensuring extensions (uuid-ossp, pgcrypto, citext)...", end=" ")
                ext_sql = "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\"; CREATE EXTENSION IF NOT EXISTS \"pgcrypto\"; CREATE EXTENSION IF NOT EXISTS \"citext\";"
                execute_sql_directly(ext_sql, "postgres", db_name, shared_creds['host'], shared_creds['port'], shared_creds['password'])
                print("Done.")
                print(f"[{idx}/{len(processed_migrations)}] Executing migration...", end=" ", flush=True)

            returncode, stdout, stderr = execute_sql_directly(
                sql, "postgres", db_name, 
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

def get_created_tables(project_id, is_shared, db_user, db_name, shared_creds=None):
    """Check what tables are now in the database."""
    print("\n🔍 Verifying created tables...")
    sql = """
        SELECT schemaname, tablename 
        FROM pg_tables 
        WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
        ORDER BY schemaname, tablename;
    """
    
    if is_shared:
        import psycopg2
        from psycopg2.extras import RealDictCursor
        try:
            conn = psycopg2.connect(
                host=shared_creds['host'],
                port=shared_creds['port'],
                user="postgres", # Use superuser for verification
                password=shared_creds['password'],
                dbname=db_name
            )
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(sql)
            tables = cursor.fetchall()
            cursor.close()
            conn.close()
            return tables
        except Exception as e:
            print(f"  ⚠️ Could not verify tables: {e}")
            return []
    else:
        container_name = f"{project_id}-postgres-1"
        cmd = ["docker", "exec", container_name, "psql", "-U", db_user, "-d", db_name, "-t", "-c", sql]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            tables = []
            for line in result.stdout.split('\n'):
                if '|' in line:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 2:
                        tables.append({'schemaname': parts[0], 'tablename': parts[1]})
            return tables
    return []

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
        import os
        db_name = f"project_{project_id}"
        db_user = f"{db_name}_user"
        shared_creds = {
            'host': os.getenv("SHARED_POSTGRES_HOST", "localhost"),
            'port': int(os.getenv("SHARED_POSTGRES_PORT", "5435")),
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
    
    # Verify tables
    tables = get_created_tables(project_id, is_shared, db_user, db_name, shared_creds)
    if tables:
        print(f"\n✨ Extracted tables ({len(tables)}):")
        for t in tables:
            print(f"   - {t['schemaname']}.{t['tablename']}")
    else:
        print("\n⚠️ No tables found after migration. They might have been created in a hidden schema or the migration only contained logic/data.")

    print("\n✨ Migration extraction complete!")
    if not is_shared:
        print(f"   Run: docker exec -i {project_id}-postgres-1 psql -U {db_user} -d {db_name} -c \"\\dt public.*\"")
    else:
        print(f"   Imports applied to shared database {db_name}.")
    print("   to verify tables were created.")

if __name__ == "__main__":
    main()
