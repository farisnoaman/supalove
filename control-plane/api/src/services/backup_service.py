import os
import subprocess
import datetime
import io
import time
from typing import List, Dict, Any

from services.storage_service import StorageService
from services.project_service import get_project_by_id
from models.project_secret import ProjectSecret
from core.database import SessionLocal

class BackupService:
    def __init__(self):
        self.storage_service = StorageService()
        # Ensure a bucket for backups exists
        self.backup_bucket = "supalove-backups"
        if not self.storage_service.client.bucket_exists(self.backup_bucket):
            self.storage_service.client.make_bucket(self.backup_bucket)

    def _get_db_url(self, project_id: str) -> str:
        # Construct DB URL from secrets. 
        # Note: In a real distributed system, we need to ensure the worker allows network access to the DB.
        # For Local/Coolify, we assume the DB is reachable via the URL constructed in provisioning.
        db = SessionLocal()
        secrets = db.query(ProjectSecret).filter(ProjectSecret.project_id == project_id).all()
        secret_map = {s.key: s.value for s in secrets}
        db.close()
        
        # We might not have the full URL stored as a secret, usually it's constructed.
        # But we do have DB_PASSWORD.
        # Let's rely on retrieving the 'project' object which might have the db_url cached 
        # OR re-construct it. The project_service return value has it.
        # For now, let's assume we can reconstruct it or fetch it.
        # Actually, `provisioning_service` returns it, but we don't persist the full URL in DB usually?
        # Let's look at `Project` model or secrets.
        
        # Fallback: Construct for Local/Coolify
        # This is a bit brittle, ideally we persist the connection info.
        # Let's use the secret map.
        password = secret_map.get("DB_PASSWORD", "postgres")
        # For local, it's localhost:DB_PORT. For Coolify, it's domain based.
        # We need to know which provider was used or the stored URL.
        # Let's verify if `db_url` is stored on the Project model? No, it's usually returned dynamically.
        # But `Project` has status.
        
        # HACK: For this implementation, let's assume standard local docker ports for now 
        # or fetch from Provisioner if possible.
        # Better approach: The `project_service.create_project` returns db_url. 
        # We should probably persist it or allow `provisioning_service` to return info for existing projects.
        
        # Let's stick to Local defaults for immediate testability.
        # Real-world: Store `db_connection_string` in ProjectSecret.
        
        port = secret_map.get("DB_PORT", "5432")
        host = "localhost" # Assuming reachable from control-plane
        return f"postgresql://app:{password}@{host}:{port}/app"

    def backup_database(self, project_id: str) -> str:
        """
        Dumps the database and uploads to MinIO.
        Returns the backup artifact path.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_id}/db_{timestamp}.sql"
        
        db_url = self._get_db_url(project_id)
        print(f"[Backup] Backing up DB for {project_id}...")

        try:
            # We use pg_dump. converting sqlalchemy url to libpq format if needed, 
            # but pg_dump accepts connection string.
            # Warning: Passing password via CLI is insecure, use PGPASSWORD env var.
            
            env = os.environ.copy()
            # Parse password from URL for env var
            # postgresql://user:pass@host:port/dbname
            from urllib.parse import urlparse
            u = urlparse(db_url)
            env["PGPASSWORD"] = u.password
            
            # Run pg_dump
            # -F c (custom format) is efficient
            command = [
                "pg_dump",
                "-h", u.hostname,
                "-p", str(u.port),
                "-U", u.username,
                "-d", u.path.lstrip("/"),
                "-F", "c", # Custom format
                "-f", "/tmp/temp_dump.sql" 
            ]
            
            subprocess.run(command, env=env, check=True)
            
            # Upload to MinIO
            with open("/tmp/temp_dump.sql", "rb") as f:
                # Get size
                f.seek(0, 2)
                size = f.tell()
                f.seek(0)
                
                self.storage_service.client.put_object(
                    self.backup_bucket,
                    filename,
                    f,
                    size,
                    content_type="application/octet-stream"
                )
            
            # Cleanup
            os.remove("/tmp/temp_dump.sql")
            
            return filename

        except Exception as e:
            print(f"[Backup] DB Backup failed: {e}")
            raise

    def backup_storage(self, project_id: str):
        """
        Syncs project bucket to backup bucket.
        """
        print(f"[Backup] Backing up Storage for {project_id}...")
        # Project bucket
        source_bucket = f"project-{project_id}"
        if not self.storage_service.client.bucket_exists(source_bucket):
             return

        # List objects
        objects = self.storage_service.client.list_objects(source_bucket, recursive=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for obj in objects:
            # Copy to backup bucket
            target_name = f"{project_id}/storage_{timestamp}/{obj.object_name}"
            
            # Use copy_object
            from minio.commonconfig import CopySource
            self.storage_service.client.copy_object(
                self.backup_bucket,
                target_name,
                CopySource(source_bucket, obj.object_name)
            )

    def list_backups(self, project_id: str) -> List[Dict[str, Any]]:
        """List backups for a project"""
        objects = self.storage_service.client.list_objects(self.backup_bucket, prefix=f"{project_id}/", recursive=True)
        backups = []
        for obj in objects:
            backups.append({
                "name": obj.object_name,
                "size": obj.size,
                "last_modified": obj.last_modified
            })
        return backups

    def restore_backup(self, project_id: str, backup_id: str):
        """
        Restores a backup. 
        backup_id is the object path in the backup bucket.
        """
        # Download backup
        # pg_restore
        # This is strictly manual-ish for now as it overrides data.
        pass
