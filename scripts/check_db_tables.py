import os
import psycopg2
from psycopg2.extras import RealDictCursor
import sys

def check_project_tables(project_id):
    db_name = f"project_{project_id}"
    db_user = "postgres"
    host = os.getenv("SHARED_POSTGRES_HOST", "localhost")
    port = int(os.getenv("SHARED_POSTGRES_PORT", "5435"))
    password = os.getenv("SHARED_POSTGRES_PASSWORD", "postgres")

    print(f"Checking database {db_name} on {host}:{port}...")
    
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=db_user,
            password=password,
            dbname=db_name
        )
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Check all tables in all schemas (except system ones)
        cursor.execute("""
            SELECT 
                schemaname, 
                tablename, 
                tableowner 
            FROM pg_tables 
            WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
            ORDER BY schemaname, tablename;
        """)
        tables = cursor.fetchall()
        
        if not tables:
            print("No tables found in any non-system schema.")
        else:
            print(f"Found {len(tables)} tables:")
            for t in tables:
                print(f"  - {t['schemaname']}.{t['tablename']} (Owned by: {t['tableowner']})")
        
        # Check schemas
        cursor.execute("SELECT nspname FROM pg_namespace WHERE nspname NOT LIKE 'pg_%%' AND nspname != 'information_schema';")
        schemas = [r['nspname'] for r in cursor.fetchall()]
        print(f"\nAvailable schemas: {', '.join(schemas)}")
        
        # Check extensions
        cursor.execute("SELECT extname FROM pg_extension;")
        extensions = [r['extname'] for r in cursor.fetchall()]
        print(f"\nInstalled extensions: {', '.join(extensions)}")
        
        # Test permissions by trying to create a table
        print("\nTesting CREATE TABLE permissions in public schema...")
        try:
            cursor.execute("CREATE TABLE public.test_perm_check (id serial PRIMARY KEY);")
            print("✅ Successfully created test table.")
            cursor.execute("DROP TABLE public.test_perm_check;")
            print("✅ Successfully dropped test table.")
        except Exception as e:
            print(f"❌ Permission check failed: {e}")
            
        # Check table ownership for existing tables
        if tables:
            print("\nTable Ownership Details:")
            for t in tables:
                print(f"  - {t['schemaname']}.{t['tablename']} : {t['tableowner']}")
        
        # Check search_path for the user
        cursor.execute("SHOW search_path;")
        print(f"\nCurrent search_path: {cursor.fetchone()['search_path']}")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_db_tables.py <project_id>")
    else:
        check_project_tables(sys.argv[1])
