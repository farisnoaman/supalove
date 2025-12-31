import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Dict, Any
from core.database import SessionLocal
from models.project import Project
from models.project_secret import ProjectSecret

class DatabaseService:
    """
    Service for connecting to and querying project databases.
    """
    
    def __init__(self, project_id: str):
        self.project_id = project_id
        self._connection = None
        
    def _get_connection_string(self) -> str:
        """Fetch database connection details from project secrets"""
        db = SessionLocal()
        try:
            # V2: Database Existence Check
            project = db.query(Project).filter(Project.id == self.project_id).first()
            if not project:
                raise ValueError(f"Project {self.project_id} does not exist in control plane.")

            # Get secrets
            secrets = db.query(ProjectSecret).filter(
                ProjectSecret.project_id == self.project_id
            ).all()
            secrets_map = {s.key: s.value for s in secrets}
            
            db_password = secrets_map.get("DB_PASSWORD")
            if not db_password:
                raise ValueError(f"Database credentials not found for project {self.project_id}")
            
            db_port = secrets_map.get("DB_PORT", "5432")
            db_user = secrets_map.get("POSTGRES_USER", "postgres")
            db_name = secrets_map.get("POSTGRES_DB", "postgres")
            
            # Use localhost for local development
            return f"postgresql://{db_user}:{db_password}@localhost:{db_port}/{db_name}"
        finally:
            db.close()
    
    def execute_query(self, sql: str) -> Dict[str, Any]:
        """
        Execute a SQL query and return results.
        Returns dict with 'rows', 'columns', 'rowCount', and 'error' keys.
        """
        try:
            conn_string = self._get_connection_string()
            
            # DEBUGGING: Log connection details
            import logging
            logger = logging.getLogger(__name__)
            logger.info(f"[SQL EDITOR DEBUG] Project ID: {self.project_id}")
            logger.info(f"[SQL EDITOR DEBUG] Connection String: {conn_string}")
            
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            # DEBUGGING: Verify which database we're actually connected to
            cursor.execute("SELECT current_database(), current_user;")
            db_info = cursor.fetchone()
            logger.info(f"[SQL EDITOR DEBUG] Connected to database: {db_info['current_database']}, user: {db_info['current_user']}")
            
            # Now execute the actual user query
            cursor.execute(sql)
            
            # Check if query returns data (SELECT, RETURNING, etc.)
            if cursor.description:
                columns = [desc[0] for desc in cursor.description]
                rows = [dict(row) for row in cursor.fetchall()]
                
                # If it was an INSERT/UPDATE/DELETE with RETURNING, we must commit!
                if sql.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                    conn.commit()
                    
                result = {
                    "rows": rows,
                    "columns": columns,
                    "rowCount": len(rows),
                    "error": None
                }
            else:
                # DDL/DML query (CREATE, INSERT, UPDATE, DELETE without RETURNING)
                conn.commit()
                result = {
                    "rows": [],
                    "columns": [],
                    "rowCount": cursor.rowcount,
                    "error": None,
                    "message": f"Query executed successfully. {cursor.rowcount} row(s) affected."
                }
            
            cursor.close()
            conn.close()
            return result
            
        except Exception as e:
            return {
                "rows": [],
                "columns": [],
                "rowCount": 0,
                "error": str(e)
            }
    
    def get_tables(self) -> List[Dict[str, Any]]:
        """Get list of all tables in the database with property status"""
        sql = """
            SELECT 
                t.table_name,
                t.table_type,
                (c.relrowsecurity) as rls_enabled,
                EXISTS (
                    SELECT 1 FROM pg_publication_tables 
                    WHERE pubname = 'supabase_realtime' 
                    AND schemaname = 'public' 
                    AND tablename = t.table_name
                ) as realtime_enabled
            FROM information_schema.tables t
            JOIN pg_class c ON c.relname = t.table_name
            JOIN pg_namespace n ON n.oid = c.relnamespace AND n.nspname = t.table_schema
            WHERE t.table_schema = 'public'
            ORDER BY t.table_name;
        """
        result = self.execute_query(sql)
        return result.get("rows", [])
    
    def get_table_schema(self, table_name: str) -> List[Dict[str, Any]]:
        """Get schema information for a specific table"""
        sql = f"""
            SELECT 
                column_name,
                data_type,
                is_nullable,
                column_default
            FROM information_schema.columns
            WHERE table_schema = 'public' 
              AND table_name = '{table_name}'
            ORDER BY ordinal_position;
        """
        result = self.execute_query(sql)
        return result.get("rows", [])

    def get_table_status(self, table_name: str) -> Dict[str, Any]:
        """Get RLS and Realtime status for a specific table"""
        sql = f"""
            SELECT 
                (c.relrowsecurity) as rls_enabled,
                EXISTS (
                    SELECT 1 FROM pg_publication_tables 
                    WHERE pubname = 'supabase_realtime' 
                    AND schemaname = 'public' 
                    AND tablename = '{table_name}'
                ) as realtime_enabled
            FROM pg_class c
            JOIN pg_namespace n ON n.oid = c.relnamespace
            WHERE n.nspname = 'public' AND c.relname = '{table_name}';
        """
        result = self.execute_query(sql)
        if result.get("rows"):
            return result["rows"][0]
        return {"rls_enabled": False, "realtime_enabled": False}
    
    def get_table_data(self, table_name: str, limit: int = 50) -> Dict[str, Any]:
        """Get sample data from a table"""
        sql = f"SELECT * FROM {table_name} LIMIT {limit};"
        return self.execute_query(sql)
    
    # RLS Policy Management
    
    def get_rls_policies(self, table_name: str) -> List[Dict[str, Any]]:
        """Get all RLS policies for a specific table"""
        sql = f"""
            SELECT
                schemaname,
                tablename,
                policyname as policy_name,
                permissive,
                roles,
                cmd as command,
                qual as using_expression,
                with_check as check_expression
            FROM pg_policies
            WHERE schemaname = 'public' 
              AND tablename = '{table_name}'
            ORDER BY policyname;
        """
        result = self.execute_query(sql)
        return result.get("rows", [])
    
    def create_rls_policy(
        self, 
        table_name: str, 
        policy_name: str,
        command: str = "ALL",
        roles: List[str] = None,
        using_expr: str = None,
        check_expr: str = None
    ) -> Dict[str, Any]:
        """Create a new RLS policy"""
        if roles is None:
            roles = ["public"]
        
        roles_str = ", ".join(roles)
        
        # Build the CREATE POLICY statement
        sql_parts = [f"CREATE POLICY \"{policy_name}\" ON public.\"{table_name}\""]
        sql_parts.append(f"FOR {command.upper()}")
        sql_parts.append(f"TO {roles_str}")
        
        if using_expr:
            sql_parts.append(f"USING ({using_expr})")
        
        if check_expr and command.upper() in ["INSERT", "UPDATE", "ALL"]:
            sql_parts.append(f"WITH CHECK ({check_expr})")
        
        sql = " ".join(sql_parts) + ";"
        
        return self.execute_query(sql)
    
    def update_rls_policy(
        self,
        table_name: str,
        policy_name: str,
        new_policy_name: str = None,
        command: str = None,
        roles: List[str] = None,
        using_expr: str = None,
        check_expr: str = None
    ) -> Dict[str, Any]:
        """
        Update an RLS policy by dropping and recreating it.
        PostgreSQL doesn't support ALTER POLICY for expressions, so we recreate.
        """
        # First, drop the existing policy
        drop_result = self.delete_rls_policy(table_name, policy_name)
        if drop_result.get("error"):
            return drop_result
        
        # Recreate with new parameters
        final_name = new_policy_name or policy_name
        return self.create_rls_policy(
            table_name=table_name,
            policy_name=final_name,
            command=command or "ALL",
            roles=roles,
            using_expr=using_expr,
            check_expr=check_expr
        )
    
    def delete_rls_policy(self, table_name: str, policy_name: str) -> Dict[str, Any]:
        """Delete an RLS policy"""
        sql = f'DROP POLICY IF EXISTS "{policy_name}" ON public."{table_name}";'
        return self.execute_query(sql)
    
    def enable_rls(self, table_name: str) -> Dict[str, Any]:
        """Enable RLS on a table"""
        sql = f'ALTER TABLE public."{table_name}" ENABLE ROW LEVEL SECURITY;'
        return self.execute_query(sql)
    
    def disable_rls(self, table_name: str) -> Dict[str, Any]:
        """Disable RLS on a table"""
        sql = f'ALTER TABLE public."{table_name}" DISABLE ROW LEVEL SECURITY;'
        return self.execute_query(sql)
    
    # Table Exploration
    
    def get_table_constraints(self, table_name: str) -> List[Dict[str, Any]]:
        """Get all constraints for a specific table"""
        sql = f"""
            SELECT
                tc.constraint_name,
                tc.constraint_type,
                kcu.column_name,
                ccu.table_name AS foreign_table_name,
                ccu.column_name AS foreign_column_name,
                rc.update_rule,
                rc.delete_rule,
                cc.check_clause
            FROM information_schema.table_constraints AS tc
            LEFT JOIN information_schema.key_column_usage AS kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
            LEFT JOIN information_schema.constraint_column_usage AS ccu
                ON ccu.constraint_name = tc.constraint_name
                AND ccu.table_schema = tc.table_schema
            LEFT JOIN information_schema.referential_constraints AS rc
                ON tc.constraint_name = rc.constraint_name
                AND tc.table_schema = rc.constraint_schema
            LEFT JOIN information_schema.check_constraints AS cc
                ON tc.constraint_name = cc.constraint_name
                AND tc.table_schema = cc.constraint_schema
            WHERE tc.table_schema = 'public'
              AND tc.table_name = '{table_name}'
            ORDER BY tc.constraint_type, tc.constraint_name;
        """
        result = self.execute_query(sql)
        return result.get("rows", [])
    
    def get_table_indexes(self, table_name: str) -> List[Dict[str, Any]]:
        """Get all indexes for a specific table"""
        sql = f"""
            SELECT
                indexname as index_name,
                indexdef as definition
            FROM pg_indexes
            WHERE schemaname = 'public'
              AND tablename = '{table_name}'
            ORDER BY indexname;
        """
        result = self.execute_query(sql)
        return result.get("rows", [])
    
    def get_table_size(self, table_name: str) -> Dict[str, Any]:
        """Get the size of a table"""
        sql = f"""
            SELECT
                pg_size_pretty(pg_total_relation_size('public."{table_name}"')) as total_size,
                pg_size_pretty(pg_relation_size('public."{table_name}"')) as table_size,
                pg_size_pretty(pg_total_relation_size('public."{table_name}"') - pg_relation_size('public."{table_name}"')) as indexes_size;
        """
        result = self.execute_query(sql)
        if result.get("rows"):
            return result["rows"][0]
        return {}

    # Realtime Management
    
    def enable_realtime(self, table_name: str) -> Dict[str, Any]:
        """Enable realtime replication for a table by adding it to the realtime publication"""
        # First, ensure the supabase_realtime publication exists
        create_pub_sql = """
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM pg_publication WHERE pubname = 'supabase_realtime') THEN
                    CREATE PUBLICATION supabase_realtime;
                END IF;
            END $$;
        """
        
        create_result = self.execute_query(create_pub_sql)
        if create_result.get("error"):
            return create_result
        
        # Add the table to the publication
        add_table_sql = f'ALTER PUBLICATION supabase_realtime ADD TABLE public."{table_name}";'
        return self.execute_query(add_table_sql)
    
    def disable_realtime(self, table_name: str) -> Dict[str, Any]:
        """Disable realtime replication for a table by removing it from the realtime publication"""
        sql = f'ALTER PUBLICATION supabase_realtime DROP TABLE public."{table_name}";'
        return self.execute_query(sql)
