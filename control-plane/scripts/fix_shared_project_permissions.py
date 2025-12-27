#!/usr/bin/env python3
"""
Fix schema permissions for existing shared projects.

This script grants the necessary permissions on the public schema
to project-specific users for all shared projects.
"""

import sys
import os

# Add parent dirs to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/api/src")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/api")

from core.database import SessionLocal
from models.project import Project, ProjectPlan, ProjectStatus
from services.shared_provisioning_service import get_custom_connection
import psycopg2
from psycopg2 import sql

def fix_permissions():
    db = SessionLocal()
    try:
        # Get all shared projects that are not deleted
        shared_projects = db.query(Project).filter(
            Project.plan == ProjectPlan.shared,
            Project.status != ProjectStatus.DELETED
        ).all()
        
        print(f"Found {len(shared_projects)} shared projects to fix")
        
        for project in shared_projects:
            if not project.db_name:
                print(f"⚠️  Project {project.id} has no db_name, skipping")
                continue
            
            db_name = project.db_name
            project_user = f"{db_name}_user"
            
            print(f"Fixing permissions for project {project.id} (db: {db_name})...")
            
            try:
                # Get cluster info
                from models.cluster import Cluster
                cluster = db.query(Cluster).filter(Cluster.id == project.cluster_id).first()
                
                if not cluster:
                    print(f"⚠️  Cluster not found for project {project.id}, using defaults")
                    host = os.getenv("SHARED_POSTGRES_HOST", "localhost")
                    port = int(os.getenv("SHARED_POSTGRES_PORT", "5435"))
                else:
                    host = cluster.postgres_host or os.getenv("SHARED_POSTGRES_HOST", "localhost")
                    port = cluster.postgres_port or int(os.getenv("SHARED_POSTGRES_PORT", "5435"))
                
                # Connect to the project database
                conn = get_custom_connection(host, port, dbname=db_name)
                conn.autocommit = True
                cursor = conn.cursor()
                
                # Grant schema permissions
                cursor.execute(
                    sql.SQL("GRANT ALL ON SCHEMA public TO {}").format(
                        sql.Identifier(project_user)
                    )
                )
                
                # Transfer schema ownership
                cursor.execute(
                    sql.SQL("ALTER SCHEMA public OWNER TO {}").format(
                        sql.Identifier(project_user)
                    )
                )
                
                print(f"✅ Fixed permissions for {project.id}")
                
                cursor.close()
                conn.close()
                
            except Exception as e:
                print(f"❌ Failed to fix {project.id}: {e}")
        
        print("\n✨ Permission fix complete!")
        
    finally:
        db.close()

if __name__ == "__main__":
    fix_permissions()
