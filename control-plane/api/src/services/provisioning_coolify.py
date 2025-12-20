import os
from pathlib import Path
from typing import Dict, Any, Optional
import httpx

from services.provisioning_interface import ProvisioningProvider

class CoolifyProvisioner(ProvisioningProvider):
    """Coolify API based provisioner"""
    
    def __init__(self, api_url: str, api_token: str):
        self.api_url = api_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        # Locate project root from this file: .../control-plane/api/src/services/provisioning_coolify.py
        # root is 4 levels up: services -> src -> api -> control-plane -> supalove
        self.project_root = Path(__file__).resolve().parents[4]
        self.templates_dir = self.project_root / "data-plane" / "templates"

    def _get_template_content(self) -> str:
        """Reads the docker-compose template file."""
        template_path = self.templates_dir / "docker-compose.project.yml"
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found at: {template_path}")
        return template_path.read_text()

    def _make_request(self, method: str, endpoint: str, data: Optional[dict] = None) -> Dict[str, Any]:
        """Helper to make HTTP requests to Coolify API"""
        url = f"{self.api_url}{endpoint}"
        try:
            with httpx.Client() as client:
                response = client.request(method, url, headers=self.headers, json=data)
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            print(f"[Coolify] Request failed: {e}")
            raise
        except httpx.HTTPStatusError as e:
            print(f"[Coolify] API error {e.response.status_code}: {e.response.text}")
            raise

    def _find_uuid_by_name(self, project_id: str) -> Optional[str]:
        """
        Finds the Coolify Application UUID for a given project_id.
        In a real scenario, we might query /api/v1/applications and filter by name.
        """
        # TODO: Implement actual lookup. 
        # For now, we assume we assume the API might give us a way to search or we store it.
        # But to be stateless, we'd search.
        # Mocking for now:
        print(f"[Coolify] Looking up UUID for project: {project_id}")
        return None 

    def provision_project(self, project_id: str, secrets: Optional[dict] = None) -> Dict[str, Any]:
        """
        Provisions a new project in Coolify.
        """
        print(f"[Coolify] Provisioning project: {project_id}")
        
        # 1. Prepare environment variables
        if secrets is None:
            secrets = {}
            
        uuid_hex = project_id
        # Simple port generation logic consistent with local provisioner (though Coolify manages internal ports)
        # We might not strictly need these for Coolify if it handles ingress, but let's keep them for consistency or env injection
        db_port = str(6000 + int(uuid_hex[:2], 16))
        rest_port = str(7000 + int(uuid_hex[:2], 16))
        realtime_port = str(8000 + int(uuid_hex[:2], 16))
        
        env_vars = {
            "PROJECT_ID": project_id,
            "DB_PASSWORD": secrets.get("DB_PASSWORD", "postgres"),
            "JWT_SECRET": secrets.get("JWT_SECRET", "super-secret-jwt-token"),
            "DB_PORT": db_port,
            "REST_PORT": rest_port,
            "REALTIME_PORT": realtime_port,
        }

        # 2. Get Docker Compose Template
        compose_content = self._get_template_content()

        # 3. Create Application in Coolify (Mocked Logic)
        # Real flow would be:
        # - Get Server UUID
        # - Get Project UUID
        # - Get Environment UUID
        # - POST /applications { ... docker_compose_raw: compose_content ... }
        
        print(f"[Coolify] deploying docker-compose for {project_id}...")
        
        # Example Payload (Hypothetical)
        payload = {
            "name": f"project-{project_id}",
            "description": f"Supalove Project {project_id}",
            "docker_compose_raw": compose_content,
            "environment_variables": env_vars,
            # "server_uuid": "...",
            # "project_uuid": "...",
            # "environment_name": "production" 
        }
        
        # self._make_request("POST", "/applications", payload)

        # 4. Construct Return URLs
        # In Coolify, we'd typically get a domain back or configure one.
        # Assuming a pattern:
        domain = "coolify.infra" 
        
        return {
            "api_url": f"https://api-{project_id}.{domain}",
            "db_url": f"postgresql://app:{env_vars['DB_PASSWORD']}@db-{project_id}.{domain}:5432/app",
            "realtime_url": f"wss://realtime-{project_id}.{domain}"
        }

    def stop_project(self, project_id: str) -> None:
        uuid = self._find_uuid_by_name(project_id)
        if uuid:
            print(f"[Coolify] Stopping application {uuid}...")
            # self._make_request("POST", f"/applications/{uuid}/stop")
        else:
            print(f"[Coolify] Could not find application for project {project_id} to stop")

    def start_project(self, project_id: str) -> None:
        uuid = self._find_uuid_by_name(project_id)
        if uuid:
            print(f"[Coolify] Starting application {uuid}...")
            # self._make_request("POST", f"/applications/{uuid}/start")
        else:
            print(f"[Coolify] Could not find application for project {project_id} to start")

    def delete_project(self, project_id: str) -> None:
        uuid = self._find_uuid_by_name(project_id)
        if uuid:
            print(f"[Coolify] Deleting application {uuid}...")
            # self._make_request("DELETE", f"/applications/{uuid}")
        else:
            print(f"[Coolify] Could not find application for project {project_id} to delete")

    def restore_project(self, project_id: str) -> None:
        print(f"[Coolify] Restore not supported via API yet for {project_id}")
