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
