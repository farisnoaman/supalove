import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Dict, Any
from core.database import SessionLocal
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
            # Get DB_PASSWORD
            password_secret = db.query(ProjectSecret).filter(
                ProjectSecret.project_id == self.project_id,
                ProjectSecret.key == "DB_PASSWORD"
            ).first()
            
            if not password_secret:
                raise ValueError(f"Database credentials not found for project {self.project_id}")
            
            # Get DB_PORT
            port_secret = db.query(ProjectSecret).filter(
                ProjectSecret.project_id == self.project_id,
                ProjectSecret.key == "DB_PORT"
            ).first()
            
            db_port = port_secret.value if port_secret else "5432"
            db_password = password_secret.value
            
            # Use host.docker.internal if in Docker, otherwise localhost
            # For local development, use localhost directly
            return f"postgresql://app:{db_password}@localhost:{db_port}/app"
        finally:
            db.close()
    
    def execute_query(self, sql: str) -> Dict[str, Any]:
        """
        Execute a SQL query and return results.
        Returns dict with 'rows', 'columns', 'rowCount', and 'error' keys.
        """
        try:
            conn_string = self._get_connection_string()
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            cursor.execute(sql)
            
            # Check if query returns data (SELECT, RETURNING, etc.)
            if cursor.description:
                columns = [desc[0] for desc in cursor.description]
                rows = [dict(row) for row in cursor.fetchall()]
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
        """Get list of all tables in the database"""
        sql = """
            SELECT 
                table_name,
                table_type
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
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
    
    def get_table_data(self, table_name: str, limit: int = 50) -> Dict[str, Any]:
        """Get sample data from a table"""
        sql = f"SELECT * FROM {table_name} LIMIT {limit};"
        return self.execute_query(sql)
