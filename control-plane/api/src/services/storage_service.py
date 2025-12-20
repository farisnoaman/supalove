import os
import json
from minio import Minio
from minio.error import S3Error

class StorageService:
    """
    Service for interacting with MinIO (S3 compatible) storage.
    """
    
    def __init__(self):
        self.endpoint = os.getenv("MINIO_ENDPOINT", "localhost:9000")
        self.access_key = os.getenv("MINIO_ROOT_USER", "minioadmin")
        self.secret_key = os.getenv("MINIO_ROOT_PASSWORD", "minioadmin")
        self.secure = os.getenv("MINIO_SECURE", "false").lower() == "true"
        self._client = None

    @property
    def client(self):
        """Lazy initialization of MinIO client"""
        if not self._client:
            try:
                self._client = Minio(
                    self.endpoint,
                    access_key=self.access_key,
                    secret_key=self.secret_key,
                    secure=self.secure
                )
            except Exception as e:
                print(f"[StorageService] Failed to connect to MinIO: {e}")
                raise
        return self._client

    def create_project_bucket(self, project_id: str) -> str:
        """
        Creates a bucket for the project.
        Returns the bucket name.
        """
        bucket_name = f"project-{project_id}"
        
        try:
            if not self.client.bucket_exists(bucket_name):
                self.client.make_bucket(bucket_name)
                print(f"[StorageService] Created bucket: {bucket_name}")
                
                # Set default policy (e.g. read-only or private)
                # For Supabase-like behavior, we often want RLS/Signed URLs,
                # but for simplicity let's leave it private (default) and rely on API keys.
            else:
                print(f"[StorageService] Bucket {bucket_name} already exists.")
                
            return bucket_name
        except S3Error as e:
            print(f"[StorageService] Error creating bucket: {e}")
            raise
    
    def list_buckets(self, project_id: str):
        """Lists all buckets for a project (structured as prefix for now)"""
        buckets = self.client.list_buckets()
        project_prefix = f"project-{project_id}"
        return [b.name for b in buckets if b.name.startswith(project_prefix)]

    def list_objects(self, project_id: str, bucket_name: str, prefix: str = None):
        """Lists objects in a project's bucket"""
        objects = self.client.list_objects(bucket_name, prefix=prefix, recursive=True)
        return [
            {
                "name": obj.object_name,
                "size": obj.size,
                "last_modified": str(obj.last_modified),
                "is_dir": obj.is_dir,
                "content_type": obj.content_type
            }
            for obj in objects
        ]

    def upload_object(self, project_id: str, bucket_name: str, object_name: str, data, length: int, content_type: str = "application/octet-stream"):
        """Uploads an object to a bucket"""
        return self.client.put_object(bucket_name, object_name, data, length, content_type=content_type)

    def delete_object(self, project_id: str, bucket_name: str, object_name: str):
        """Deletes an object from a bucket"""
        return self.client.remove_object(bucket_name, object_name)

    def get_storage_config(self, bucket_name: str) -> dict:
        """
        Returns configuration needed for the project stack to access this bucket.
        """
        return {
            "S3_ENDPOINT": self.endpoint,
            "S3_BUCKET": bucket_name,
            "S3_ACCESS_KEY": self.access_key, # In prod, create a specific user!
            "S3_SECRET_KEY": self.secret_key, # In prod, create a specific user!
            "S3_REGION": "us-east-1"
        }
