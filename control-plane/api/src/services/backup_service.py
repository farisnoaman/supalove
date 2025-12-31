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
        """
        Construct DB URL from project secrets.
        Works for both shared and dedicated projects.
        """
        db = SessionLocal()
        try:
            secrets = db.query(ProjectSecret).filter(ProjectSecret.project_id == project_id).all()
            secret_map = {s.key: s.value for s in secrets}
            
            # Get database connection details from secrets
            db_host = secret_map.get("DB_HOST", "localhost")
            db_port = secret_map.get("DB_PORT", "5432")
            db_name = secret_map.get("POSTGRES_DB", "postgres")
            db_user = secret_map.get("POSTGRES_USER", "postgres")
            db_password = secret_map.get("DB_PASSWORD", "postgres")
            
            # Construct PostgreSQL URL
            return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        finally:
            db.close()

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
        Restores a database backup.
        backup_id is the object path in the backup bucket (e.g., "project_id/db_20240101_120000.sql")
        
        WARNING: This will overwrite the current database!
        """
        print(f"[Backup] Restoring backup {backup_id} for project {project_id}...")
        
        db_url = self._get_db_url(project_id)
        
        try:
            # Download backup from MinIO
            response = self.storage_service.client.get_object(self.backup_bucket, backup_id)
            
            # Save to temp file
            temp_file = "/tmp/restore_backup.sql"
            with open(temp_file, "wb") as f:
                for data in response.stream(32*1024):
                    f.write(data)
            
            # Parse DB URL for pg_restore
            from urllib.parse import urlparse
            u = urlparse(db_url)
            
            env = os.environ.copy()
            env["PGPASSWORD"] = u.password
            
            # Use pg_restore for custom format backups
            command = [
                "pg_restore",
                "-h", u.hostname,
                "-p", str(u.port),
                "-U", u.username,
                "-d", u.path.lstrip("/"),
                "--clean",  # Drop existing objects before restore
                "--if-exists",  # Don't error if objects don't exist
                "--no-owner",   # Do not attempt to set ownership
                "--no-acl",     # Do not restore access privileges (grant/revoke)
                temp_file
            ]
            
            # Allow exit code 1 (warnings) as success
            result = subprocess.run(command, env=env, check=False, capture_output=True, text=True)
            
            if result.returncode > 1:
                # Real failure
                raise Exception(f"pg_restore failed with code {result.returncode}: {result.stderr}")
            elif result.returncode == 1:
                # Warnings (safe to ignore usually)
                print(f"[Backup] Restore finished with warnings: {result.stderr}")
            else:
                # Success (code 0)
                print(f"[Backup] Restore completed successfully")
            
            # Cleanup
            os.remove(temp_file)
            
            return {"status": "success", "message": "Database restored successfully"}
            
        except Exception as e:
            print(f"[Backup] Restore failed: {e}")
            if os.path.exists("/tmp/restore_backup.sql"):
                os.remove("/tmp/restore_backup.sql")
            raise
    
    def download_backup(self, project_id: str, backup_id: str):
        """
        Get a presigned URL to download a backup file.
        Returns a temporary download URL valid for 1 hour.
        """
        try:
            # Generate presigned URL for download
            from datetime import timedelta
            url = self.storage_service.client.presigned_get_object(
                self.backup_bucket,
                backup_id,
                expires=timedelta(hours=1)
            )
            return {"download_url": url, "expires_in": "1 hour"}
        except Exception as e:
            print(f"[Backup] Download URL generation failed: {e}")
            raise
