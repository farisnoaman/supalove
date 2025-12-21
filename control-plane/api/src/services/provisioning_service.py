import os
from services.provisioning_interface import Provisioner
from services.provisioning_local import LocalProvisioner
from services.provisioning_coolify import CoolifyProvisioner

def _get_provider() -> Provisioner:
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

def provision_project(project_id: str, secrets: dict = None, custom_domain: str = None) -> dict:
    """
    Orchestrates provisioning of a project runtime.
    """
    if secrets is None:
        secrets = {}
    
    return _provider.provision(project_id, secrets, custom_domain=custom_domain)

def stop_project(project_id: str):
    return _provider.stop(project_id)

def start_project(project_id: str):
    return _provider.start(project_id)

def delete_project(project_id: str):
    return _provider.destroy(project_id)

def restore_project(project_id: str):
    return _provider.restore(project_id)
