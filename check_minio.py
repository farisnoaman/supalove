## Example usage:
#./control-plane/api/.venv/bin/python3 check_minio.py
#./control-plane/api/.venv/bin/python3 check_auth.py 29315029c9e7
###########
from minio import Minio
import os

client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

buckets = client.list_buckets()
print(f"Found {len(buckets)} buckets:")
for b in buckets:
    print(f" - {b.name}")

# Example logic to ensure a test project has its bucket
project_id = "29315029c9e7"
bucket_name = f"project-{project_id}"
if not client.bucket_exists(bucket_name):
    print(f"Creating missing bucket: {bucket_name}")
    client.make_bucket(bucket_name)
else:
    print(f"Bucket {bucket_name} already exists.")
