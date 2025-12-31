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
SHARED_POSTGRES_PORT = int(os.getenv("SHARED_POSTGRES_PORT", "5435"))
SHARED_POSTGRES_USER = os.getenv("SHARED_POSTGRES_USER", "postgres")
SHARED_POSTGRES_PASSWORD = os.getenv("SHARED_POSTGRES_PASSWORD", "postgres")
SHARED_POSTGRES_ADMIN_DB = os.getenv("SHARED_POSTGRES_ADMIN_DB", "postgres")

# Shared gateway URL for API access
SHARED_GATEWAY_URL = os.getenv("SHARED_GATEWAY_URL", "http://localhost:8081")


def get_admin_connection():
    """Get a connection to the shared Postgres cluster as admin."""
    return psycopg2.connect(
        host=SHARED_POSTGRES_HOST,
        port=SHARED_POSTGRES_PORT,
        user=SHARED_POSTGRES_USER,
        password=SHARED_POSTGRES_PASSWORD,
        dbname=SHARED_POSTGRES_ADMIN_DB,
    )


def get_custom_connection(host, port, dbname=None, user=None, password=None):
    return psycopg2.connect(
        host=host,
        port=port,
        user=user or SHARED_POSTGRES_USER,
        password=password or SHARED_POSTGRES_PASSWORD,
        dbname=dbname or SHARED_POSTGRES_ADMIN_DB,
    )

def create_project_database(db_name: str, db_password: str, host: str, port: int) -> None:
    """
    Create a new database in the targeted Postgres cluster.
    """
    conn = get_custom_connection(host, port)
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
        
        # Grant privileges on database
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
    # Schema-specific permissions will be granted in apply_supabase_migrations
    # after the schemas are created.
    print(f"[SharedProvisioning] Database {db_name} and role {project_user} prepared")


def apply_supabase_migrations(db_name: str, db_password: str, host: str, port: int) -> None:
    """
    Apply Supabase-compatible migrations to the project database.
    """
    conn = get_custom_connection(host, port, dbname=db_name)
    cursor = conn.cursor()
    
    try:
        # Create Supabase-required schemas
        project_user = f"{db_name}_user"
        migrations = f"""
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
            CREATE ROLE authenticator NOINHERIT LOGIN PASSWORD '{db_password}';
        EXCEPTION WHEN duplicate_object THEN NULL;
        END $$;
        
        -- Grant schema access to project roles
        GRANT USAGE ON SCHEMA public TO anon, authenticated, service_role;
        GRANT USAGE ON SCHEMA auth TO anon, authenticated, service_role;
        GRANT USAGE ON SCHEMA storage TO anon, authenticated, service_role;
        
        -- Allow authenticator to switch roles
        GRANT anon TO authenticator;
        GRANT authenticated TO authenticator;
        GRANT service_role TO authenticator;
        
        -- Grant schema access to the project user (the one used for migrations and SQL editor)
        GRANT USAGE, CREATE ON SCHEMA public TO {project_user};
        GRANT USAGE, CREATE ON SCHEMA auth TO {project_user};
        GRANT USAGE, CREATE ON SCHEMA storage TO {project_user};
        GRANT USAGE, CREATE ON SCHEMA _realtime TO {project_user};
        
        -- Enable Row Level Security functionality
        ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO anon, authenticated, service_role;
        ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO anon, authenticated, service_role;
        ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO anon, authenticated, service_role;
        
        -- ============================================
        -- AUTH.USERS TABLE (Supabase Compatible)
        -- ============================================
        CREATE TABLE IF NOT EXISTS auth.users (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            email TEXT UNIQUE NOT NULL,
            encrypted_password TEXT NOT NULL,
            created_at TIMESTAMPTZ DEFAULT NOW(),
            updated_at TIMESTAMPTZ DEFAULT NOW(),
            email_confirmed_at TIMESTAMPTZ,
            last_sign_in_at TIMESTAMPTZ,
            role TEXT DEFAULT 'authenticated',
            aud TEXT DEFAULT 'authenticated',
            user_metadata JSONB DEFAULT '{{}}',
            app_metadata JSONB DEFAULT '{{}}'
        );
        
        -- Create auth.uid() function for RLS policies
        CREATE OR REPLACE FUNCTION auth.uid() 
        RETURNS UUID 
        LANGUAGE sql STABLE
        AS $$
            SELECT NULLIF(current_setting('request.jwt.claim.sub', true), '')::uuid
        $$;
        
        -- Create auth.role() function for RLS policies
        CREATE OR REPLACE FUNCTION auth.role() 
        RETURNS TEXT 
        LANGUAGE sql STABLE
        AS $$
            SELECT NULLIF(current_setting('request.jwt.claim.role', true), '')::text
        $$;
        
        -- Create auth.jwt() function for RLS policies
        CREATE OR REPLACE FUNCTION auth.jwt() 
        RETURNS JSONB 
        LANGUAGE sql STABLE
        AS $$
            SELECT COALESCE(
                current_setting('request.jwt.claims', true),
                '{{}}'
            )::jsonb
        $$;
        
        GRANT ALL ON ALL TABLES IN SCHEMA auth TO {project_user};
        GRANT ALL ON ALL SEQUENCES IN SCHEMA auth TO {project_user};
        GRANT EXECUTE ON FUNCTION auth.uid() TO anon, authenticated, service_role, {project_user};
        GRANT EXECUTE ON FUNCTION auth.role() TO anon, authenticated, service_role, {project_user};
        GRANT EXECUTE ON FUNCTION auth.jwt() TO anon, authenticated, service_role, {project_user};

        -- ============================================
        -- STORAGE TABLES
        -- ============================================
        CREATE TABLE IF NOT EXISTS storage.buckets (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            owner UUID,
            created_at TIMESTAMPTZ DEFAULT NOW(),
            updated_at TIMESTAMPTZ DEFAULT NOW(),
            public BOOLEAN DEFAULT FALSE,
            avif_autoprovision BOOLEAN DEFAULT FALSE,
            file_size_limit BIGINT,
            allowed_mime_types TEXT[]
        );

        CREATE TABLE IF NOT EXISTS storage.objects (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            bucket_id TEXT REFERENCES storage.buckets(id),
            name TEXT,
            owner UUID,
            created_at TIMESTAMPTZ DEFAULT NOW(),
            updated_at TIMESTAMPTZ DEFAULT NOW(),
            last_accessed_at TIMESTAMPTZ DEFAULT NOW(),
            metadata JSONB,
            path_tokens TEXT[] GENERATED ALWAYS AS (string_to_array(name, '/')) STORED
        );

        GRANT ALL ON ALL TABLES IN SCHEMA storage TO {project_user};
        GRANT ALL ON ALL SEQUENCES IN SCHEMA storage TO {project_user};

        -- ============================================
        -- REALTIME PUBLICATION
        -- ============================================
        DO $$ BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_publication WHERE pubname = 'supabase_realtime') THEN
                CREATE PUBLICATION supabase_realtime;
            END IF;
        EXCEPTION WHEN OTHERS THEN 
            RAISE NOTICE 'Could not create publication';
        END $$;
        """
        
        cursor.execute(migrations)
        conn.commit()
        print(f"[SharedProvisioning] Applied full migrations to {db_name}")
        
    finally:
        cursor.close()
        conn.close()


def provision_shared_project(db: Session, project: Project, cluster: Any, secrets: Dict[str, Any]) -> Dict[str, Any]:
    """
    Provision a shared project in a specific cluster.
    
    This:
    1. Creates a new database in the specified cluster
    2. Applies Supabase migrations
    3. Does NOT start any containers
    
    Args:
        db: Database session
        project: Project model instance
        cluster: Cluster model instance
        secrets: Project secrets including JWT_SECRET, DB_PASSWORD, etc.
    
    Returns:
        Dictionary with API URL and DB connection info
    """
    db_name = project.db_name
    db_password = secrets.get("DB_PASSWORD", "postgres")
    
    host = cluster.postgres_host or SHARED_POSTGRES_HOST
    port = cluster.postgres_port or SHARED_POSTGRES_PORT
    api_url = cluster.api_url or SHARED_GATEWAY_URL
    
    print(f"[SharedProvisioning] Provisioning shared project: {project.id} in cluster {cluster.id}")
    
    # 1. Create the database
    create_project_database(db_name, db_password, host=host, port=port)
    
    # 2. Apply Supabase migrations
    apply_supabase_migrations(db_name, db_password, host=host, port=port)
    
    print(f"[SharedProvisioning] Shared project {project.id} provisioned successfully")
    
    # Return connection info for shared gateway
    return {
        "api_url": f"{api_url}/projects/{project.id}",
        "db_url": f"postgresql://{db_name}_user:{db_password}@{host}:{port}/{db_name}",
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
