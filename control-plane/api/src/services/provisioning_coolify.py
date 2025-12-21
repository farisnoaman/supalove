import os
import time
from pathlib import Path
from typing import Dict, Any, Optional
import httpx

from services.provisioning_interface import Provisioner

class CoolifyProvisioner(Provisioner):
    """Coolify API based provisioner for V4"""

    def __init__(self, api_url: str, api_token: str):
        self.api_url = api_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
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
            with httpx.Client(timeout=30.0) as client:
                response = client.request(method, url, headers=self.headers, json=data)
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            print(f"[Coolify] Request failed: {e}")
            raise
        except httpx.HTTPStatusError as e:
            print(f"[Coolify] API error {e.response.status_code}: {e.response.text}")
            raise

    def _get_first_server(self) -> str:
        """Fetches the first available server UUID"""
        servers = self._make_request("GET", "/api/v1/servers")
        if not servers:
            raise Exception("No servers found in Coolify")
        return servers[0]["uuid"]

    def _ensure_project_and_env(self, project_name: str = "Supalove Users") -> tuple[str, str]:
        """
        Ensures a project and 'production' environment exist.
        Returns (project_uuid, environment_name).
        """
        projects = self._make_request("GET", "/api/v1/projects")
        target_project = next((p for p in projects if p["name"] == project_name), None)

        if not target_project:
            print(f"[Coolify] Creating project: {project_name}")
            target_project = self._make_request("POST", "/api/v1/projects", {"name": project_name})
        
        project_uuid = target_project["uuid"]
        
        # In Coolify V4, we typically get the default environment (usually 'production')
        # Here we just return the name 'production' as it's often the default key
        return project_uuid, "production"

    def _find_resource_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Finds a resource (application) by its name"""
        resources = self._make_request("GET", "/api/v1/resources")
        # Resources list might be flat or nested, depends on API version. 
        # Assuming flat list of all resources.
        for res in resources:
            if res.get("name") == name:
                return res
        return None

    def provision(self, project_id: str, secrets: Optional[dict] = None, custom_domain: Optional[str] = None) -> Dict[str, Any]:
        """Provisions a new project in Coolify."""
        print(f"[Coolify] Provisioning project: {project_id}")
        
        if secrets is None:
            secrets = {}

        compose_content = self._get_template_content()
        resource_name = f"project-{project_id}"
        
        # Check if already exists
        existing = self._find_resource_by_name(resource_name)
        if existing:
            print(f"[Coolify] Resource {resource_name} already exists. UUID: {existing['uuid']}")
            # In a real impl, we might update config here.
            # return self._construct_return_urls(existing)
            # For now, let's fall through to update/re-deploy logic if needed, 
            # or just return success if it's running.
            pass

        server_uuid = self._get_first_server()
        project_uuid, env_name = self._ensure_project_and_env()

        # Create Application (Docker Compose)
        # Note: The endpoint might be /api/v1/projects/{uuid}/{env_name}/applications
        # Or a general create endpoint.
        # Specifics depend on exact Coolify version. using /applications/compose based on common V4 patterns.
        
        payload = {
            "project_uuid": project_uuid,
            "server_uuid": server_uuid,
            "environment_name": env_name,
            "name": resource_name,
            "description": f"Supalove Project {project_id}",
            "docker_compose_raw": compose_content,
        }
        
        print(f"[Coolify] Creating application {resource_name}...")
        try:
             # Try creating via the applications endpoint
            app_response = self._make_request("POST", "/api/v1/applications/compose", payload)
            app_uuid = app_response["uuid"]
        except Exception:
             # Fallback or different endpoint strategy if needed
             # For now, assume success or raise
             raise

        # Set Environment Variables
        # /api/v1/applications/{uuid}/envs
        print(f"[Coolify] Setting environment variables for {app_uuid}...")
        env_vars = {
            "PROJECT_ID": project_id,
            "DB_PASSWORD": secrets.get("DB_PASSWORD", "postgres"),
            "JWT_SECRET": secrets.get("JWT_SECRET", "super-secret-jwt-token"),
            # Coolify handles ports internally for ingress usually, 
            # but if we use host networking or specific ports in compose:
            # "DB_PORT": ... 
        }
        
        for key, value in env_vars.items():
            self._make_request("POST", f"/api/v1/applications/{app_uuid}/envs", {
                "key": key,
                "value": str(value),
                "is_build_time": False,
                "is_literal": True
            })

        # Deploy
        # Deploy
        print(f"[Coolify] Deploying {app_uuid}...")
        self._make_request("POST", f"/api/v1/applications/{app_uuid}/deploy")
        
        # Configure Custom Domain if provided
        final_url = None
        domain_suffix = "coolify.infra" 

        if custom_domain:
            print(f"[Coolify] Setting custom domain: {custom_domain} for {app_uuid}")
            # Assumption: Coolify V4 allows setting FQDN via settings or similar
            # Ideally: PATCH /api/v1/applications/{uuid} with {"fqdn": custom_domain}
            try:
                self._make_request("PATCH", f"/api/v1/applications/{app_uuid}", {"fqdn": custom_domain})
                final_url = f"https://{custom_domain}"
            except Exception as e:
                print(f"[Coolify] Failed to set custom domain: {e}")
                # Fallback to default
        
        if not final_url:
            # FallbackURL
            final_url = f"https://{resource_name}.{domain_suffix}"

        return {
            "api_url": final_url,
            "db_url": f"postgresql://app:{env_vars['DB_PASSWORD']}@db-{project_id}.{domain_suffix}:5432/app",
        }

    def stop(self, project_id: str) -> None:
        resource = self._find_resource_by_name(f"project-{project_id}")
        if resource:
            print(f"[Coolify] Stopping {resource['name']} ({resource['uuid']})...")
            self._make_request("POST", f"/api/v1/applications/{resource['uuid']}/stop")

    def start(self, project_id: str) -> None:
        resource = self._find_resource_by_name(f"project-{project_id}")
        if resource:
            print(f"[Coolify] Starting {resource['name']} ({resource['uuid']})...")
            self._make_request("POST", f"/api/v1/applications/{resource['uuid']}/start")

    def destroy(self, project_id: str) -> None:
        resource = self._find_resource_by_name(f"project-{project_id}")
        if resource:
            print(f"[Coolify] Deleting {resource['name']} ({resource['uuid']})...")
            self._make_request("DELETE", f"/api/v1/applications/{resource['uuid']}")

    def restore(self, project_id: str) -> None:
        print("[Coolify] Restore not supported via API yet")
