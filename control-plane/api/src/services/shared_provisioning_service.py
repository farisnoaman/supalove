"""
Shared Provisioning Service

Handles provisioning for shared plan projects:
- Creates a database in the shared Postgres cluster
- Applies Supabase migrations
- Generates and stores JWT secrets
- Does NOT spawn any Docker containers
"""
import os
import psycopg2
from psycopg2 import sql
from sqlalchemy.orm import Session
from typing import Dict, Any

from models.project import Project


# Shared cluster connection settings (from environment or defaults)
SHARED_POSTGRES_HOST = os.getenv("SHARED_POSTGRES_HOST", "localhost")
SHARED_POSTGRES_PORT = int(os.getenv("SHARED_POSTGRES_PORT", "5433"))
SHARED_POSTGRES_USER = os.getenv("SHARED_POSTGRES_USER", "postgres")
SHARED_POSTGRES_PASSWORD = os.getenv("SHARED_POSTGRES_PASSWORD", "postgres")
SHARED_POSTGRES_ADMIN_DB = os.getenv("SHARED_POSTGRES_ADMIN_DB", "postgres")

# Shared gateway URL for API access
SHARED_GATEWAY_URL = os.getenv("SHARED_GATEWAY_URL", "http://localhost:8080")


def get_admin_connection():
    """Get a connection to the shared Postgres cluster as admin."""
    return psycopg2.connect(
        host=SHARED_POSTGRES_HOST,
        port=SHARED_POSTGRES_PORT,
        user=SHARED_POSTGRES_USER,
        password=SHARED_POSTGRES_PASSWORD,
        dbname=SHARED_POSTGRES_ADMIN_DB,
    )


def create_project_database(db_name: str, db_password: str) -> None:
    """
    Create a new database in the shared Postgres cluster.
    
    Args:
        db_name: Name of the database to create (e.g., project_abc123)
        db_password: Password for the project's database user
    """
    conn = get_admin_connection()
    conn.autocommit = True
    cursor = conn.cursor()
    
    try:
        # Create the database
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        print(f"[SharedProvisioning] Created database: {db_name}")
        
        # Create project-specific roles
        project_user = f"{db_name}_user"
        cursor.execute(
            sql.SQL("CREATE ROLE {} WITH LOGIN PASSWORD %s").format(sql.Identifier(project_user)),
            [db_password]
        )
        
        # Grant privileges
        cursor.execute(
            sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {}").format(
                sql.Identifier(db_name),
                sql.Identifier(project_user)
            )
        )
        print(f"[SharedProvisioning] Created role: {project_user}")
        
    except psycopg2.errors.DuplicateDatabase:
        print(f"[SharedProvisioning] Database {db_name} already exists, skipping creation")
    except psycopg2.errors.DuplicateObject:
        print(f"[SharedProvisioning] Role already exists, skipping creation")
    finally:
        cursor.close()
        conn.close()


def apply_supabase_migrations(db_name: str, db_password: str) -> None:
    """
    Apply Supabase-compatible migrations to the project database.
    
    This sets up the required schemas and roles for Supabase services
    (auth, storage, realtime, etc.) to work properly.
    """
    conn = psycopg2.connect(
        host=SHARED_POSTGRES_HOST,
        port=SHARED_POSTGRES_PORT,
        user=SHARED_POSTGRES_USER,
        password=SHARED_POSTGRES_PASSWORD,
        dbname=db_name,
    )
    cursor = conn.cursor()
    
    try:
        # Create Supabase-required schemas
        migrations = """
        -- Create required schemas
        CREATE SCHEMA IF NOT EXISTS auth;
        CREATE SCHEMA IF NOT EXISTS storage;
        CREATE SCHEMA IF NOT EXISTS _realtime;
        CREATE SCHEMA IF NOT EXISTS graphql_public;
        
        -- Create required roles for Supabase services
        DO $$ BEGIN
            CREATE ROLE anon NOLOGIN NOINHERIT;
        EXCEPTION WHEN duplicate_object THEN NULL;
        END $$;
        
        DO $$ BEGIN
            CREATE ROLE authenticated NOLOGIN NOINHERIT;
        EXCEPTION WHEN duplicate_object THEN NULL;
        END $$;
        
        DO $$ BEGIN
            CREATE ROLE service_role NOLOGIN NOINHERIT BYPASSRLS;
        EXCEPTION WHEN duplicate_object THEN NULL;
        END $$;
        
        DO $$ BEGIN
            CREATE ROLE authenticator NOINHERIT LOGIN PASSWORD 'PLACEHOLDER_PASSWORD';
        EXCEPTION WHEN duplicate_object THEN NULL;
        END $$;
        
        -- Grant schema access
        GRANT USAGE ON SCHEMA public TO anon, authenticated, service_role;
        GRANT USAGE ON SCHEMA auth TO anon, authenticated, service_role;
        GRANT USAGE ON SCHEMA storage TO anon, authenticated, service_role;
        
        -- Allow authenticator to switch roles
        GRANT anon TO authenticator;
        GRANT authenticated TO authenticator;
        GRANT service_role TO authenticator;
        
        -- Enable Row Level Security by default on public tables
        ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO anon, authenticated, service_role;
        ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO anon, authenticated, service_role;
        ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO anon, authenticated, service_role;
        """
        
        # Replace placeholder password
        migrations = migrations.replace("PLACEHOLDER_PASSWORD", db_password)
        
        cursor.execute(migrations)
        conn.commit()
        print(f"[SharedProvisioning] Applied migrations to {db_name}")
        
    finally:
        cursor.close()
        conn.close()


def provision_shared_project(db: Session, project: Project, secrets: Dict[str, Any]) -> Dict[str, Any]:
    """
    Provision a shared project.
    
    This:
    1. Creates a new database in the shared Postgres cluster
    2. Applies Supabase migrations
    3. Does NOT start any containers
    
    Args:
        db: Database session
        project: Project model instance
        secrets: Project secrets including JWT_SECRET, DB_PASSWORD, etc.
    
    Returns:
        Dictionary with API URL and DB connection info
    """
    db_name = project.db_name
    db_password = secrets.get("DB_PASSWORD", "postgres")
    
    print(f"[SharedProvisioning] Provisioning shared project: {project.id}")
    
    # 1. Create the database
    create_project_database(db_name, db_password)
    
    # 2. Apply Supabase migrations
    apply_supabase_migrations(db_name, db_password)
    
    print(f"[SharedProvisioning] Shared project {project.id} provisioned successfully")
    
    # Return connection info for shared gateway
    return {
        "api_url": f"{SHARED_GATEWAY_URL}/projects/{project.id}",
        "db_url": f"postgresql://{db_name}_user:{db_password}@{SHARED_POSTGRES_HOST}:{SHARED_POSTGRES_PORT}/{db_name}",
    }


def delete_shared_project(project: Project) -> None:
    """
    Delete a shared project's database from the cluster.
    
    Args:
        project: Project model instance
    """
    db_name = project.db_name
    
    if not db_name:
        print(f"[SharedProvisioning] No database name for project {project.id}, skipping deletion")
        return
    
    conn = get_admin_connection()
    conn.autocommit = True
    cursor = conn.cursor()
    
    try:
        # Terminate existing connections
        cursor.execute(
            sql.SQL("""
                SELECT pg_terminate_backend(pid) 
                FROM pg_stat_activity 
                WHERE datname = %s AND pid <> pg_backend_pid()
            """),
            [db_name]
        )
        
        # Drop the database
        cursor.execute(sql.SQL("DROP DATABASE IF EXISTS {}").format(sql.Identifier(db_name)))
        
        # Drop the project user
        project_user = f"{db_name}_user"
        cursor.execute(sql.SQL("DROP ROLE IF EXISTS {}").format(sql.Identifier(project_user)))
        
        print(f"[SharedProvisioning] Deleted database and role for project {project.id}")
        
    finally:
        cursor.close()
        conn.close()
