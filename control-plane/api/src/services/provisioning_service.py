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

# Global provider instance
_provider = _get_provider()

def provision_project(project_id: str, secrets: dict):
    """
    Orchestrates provisioning of a project runtime.
    Delegates to the configured provider (Local or Coolify).
    """
    return _provider.provision_project(project_id, secrets)

def stop_project(project_id: str):
    return _provider.stop_project(project_id)

def start_project(project_id: str):
    return _provider.start_project(project_id)

def delete_project(project_id: str):
    return _provider.delete_project(project_id)

def restore_project(project_id: str):
    return _provider.restore_project(project_id)
