import sys
from pathlib import Path
import psycopg2

# Add src to path
PROJECT_ROOT = Path(__file__).resolve().parents[0]
sys.path.append(str(PROJECT_ROOT))

from services.database_service import DatabaseService

# Fixed project ID from user interaction
PROJECT_ID = "29315029c9e7"

def fix_roles():
    print(f"Fixing roles for project {PROJECT_ID}...")
    try:
        db = DatabaseService(PROJECT_ID)
        
        sql = """
        DO $$
        BEGIN
          IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'anon') THEN
            CREATE ROLE anon NOLOGIN;
          END IF;
          IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'authenticated') THEN
            CREATE ROLE authenticated NOLOGIN;
          END IF;
          IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'service_role') THEN
            CREATE ROLE service_role NOLOGIN;
          END IF;
        END
        $$;

        GRANT USAGE ON SCHEMA public TO anon;
        GRANT USAGE ON SCHEMA public TO authenticated;
        GRANT USAGE ON SCHEMA public TO service_role;

        GRANT ALL ON ALL TABLES IN SCHEMA public TO anon;
        GRANT ALL ON ALL TABLES IN SCHEMA public TO authenticated;
        GRANT ALL ON ALL TABLES IN SCHEMA public TO service_role;
        
        ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO anon;
        ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO authenticated;
        ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO service_role;

        GRANT anon TO app;
        GRANT authenticated TO app;
        GRANT service_role TO app;
        """
        
        result = db.execute_query(sql)
        if result.get("error"):
            print(f"Error executing fix: {result['error']}")
        else:
            print("Successfully created/verified roles.")
            
    except Exception as e:
        print(f"Exception: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_roles()
