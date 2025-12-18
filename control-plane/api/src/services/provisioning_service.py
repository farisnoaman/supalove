import os
from services.provisioning_interface import ProvisioningProvider
from services.provisioning_local import LocalProvisioner
from services.provisioning_coolify import CoolifyProvisioner

def _get_provider() -> ProvisioningProvider:
    """
    Factory function to get the appropriate provisioning provider
    based on environment variables.
    """
    coolify_url = os.getenv("COOLIFY_API_URL")
    coolify_token = os.getenv("COOLIFY_API_TOKEN")
    
    if coolify_url and coolify_token:
        print(f"[Provisioning] Using Coolify provider: {coolify_url}")
        return CoolifyProvisioner(coolify_url, coolify_token)
    else:
        print("[Provisioning] Using Local Docker provider")
        return LocalProvisioner()

from services.auth_service import AuthService
from services.storage_service import StorageService

# Global providers
_provider = _get_provider()
_auth_service = AuthService()
_storage_service = StorageService()

def provision_project(project_id: str, secrets: dict = None):
    """
    Orchestrates provisioning of a project runtime.
    1. Creates Auth Realm & Client (Keycloak)
    2. Provision Storage Bucket (MinIO)
    3. Provisions Infrastructure (Docker/Coolify)
    """
    if secrets is None:
        secrets = {}

    try:
        # 1. Auth Provisioning
        print(f"[Provisioning] Setting up Auth for {project_id}...")
        realm = _auth_service.create_project_realm(project_id)
        client_info = _auth_service.create_api_client(realm)
        
        jwt_secret = _auth_service.get_jwt_secret(realm)
        secrets["JWT_SECRET"] = jwt_secret
        secrets["SERVICE_ROLE_KEY"] = client_info["client_secret"]
        
    except Exception as e:
        print(f"[Provisioning] Auth setup failed (continuing with placeholders): {e}")
        if "JWT_SECRET" not in secrets:
            secrets["JWT_SECRET"] = "fallback-secret-for-dev"

    try:
        # 2. Storage Provisioning
        print(f"[Provisioning] Setting up Storage for {project_id}...")
        bucket = _storage_service.create_project_bucket(project_id)
        storage_config = _storage_service.get_storage_config(bucket)
        
        # Merge storage config into secrets/env
        secrets.update(storage_config)

    except Exception as e:
        print(f"[Provisioning] Storage setup failed: {e}")

    # 3. Infra Provisioning
    return _provider.provision_project(project_id, secrets)

def stop_project(project_id: str):
    return _provider.stop_project(project_id)

def start_project(project_id: str):
    return _provider.start_project(project_id)

def delete_project(project_id: str):
    return _provider.delete_project(project_id)

def restore_project(project_id: str):
    return _provider.restore_project(project_id)
