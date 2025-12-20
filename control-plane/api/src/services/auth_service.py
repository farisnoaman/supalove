import os
import secrets
from keycloak import KeycloakAdmin
from keycloak.exceptions import KeycloakError

class AuthService:
    """
    Service for interacting with Keycloak to manage project authentication.
    """
    
    def __init__(self):
        self.server_url = os.getenv("KEYCLOAK_URL", "http://localhost:8080/")
        self.username = os.getenv("KEYCLOAK_ADMIN", "admin")
        self.password = os.getenv("KEYCLOAK_ADMIN_PASSWORD", "admin")
        self.realm_name = "master"
        self._admin = None

    def _get_admin(self, realm_name: str = None) -> KeycloakAdmin:
        """Helper to get a KeycloakAdmin instance for a specific realm"""
        return KeycloakAdmin(
            server_url=self.server_url,
            username=self.username,
            password=self.password,
            realm_name=realm_name or self.realm_name,
            user_realm_name="master",
            verify=True
        )

    @property
    def admin(self):
        """Lazy initialization of KeycloakAdmin client for the master realm"""
        if not self._admin:
            try:
                self._admin = self._get_admin()
            except Exception as e:
                print(f"[AuthService] Failed to connect to Keycloak: {e}")
                raise
        return self._admin

    def create_project_realm(self, project_id: str) -> str:
        """
        Creates a new realm for the project.
        Returns the realm name.
        """
        realm_name = f"project-{project_id}"
        try:
            # Check if realm exists
            self.admin.get_realm(realm_name)
            print(f"[AuthService] Realm {realm_name} already exists.")
            return realm_name
        except KeycloakError:
            pass # Realm doesn't exist, proceed to create

        payload = {
            "realm": realm_name,
            "enabled": True,
            "displayName": f"Project {project_id}",
        }
        self.admin.create_realm(payload=payload)
        print(f"[AuthService] Created realm: {realm_name}")
        return realm_name

    def create_api_client(self, realm_name: str) -> dict:
        """
        Creates an OIDC client for the project API in the specified realm.
        Returns client secrets.
        """
        client_id = "api-service"
        realm_admin = self._get_admin(realm_name=realm_name)
        
        # Check if client exists
        clients = realm_admin.get_clients()
        existing = next((c for c in clients if c.get("clientId") == client_id), None)
        
        if existing:
            client_uuid = existing["id"]
        else:
            payload = {
                "clientId": client_id,
                "name": "API Service",
                "enabled": True,
                "clientAuthenticatorType": "client-secret",
                "secret": secrets.token_urlsafe(32),
                "serviceAccountsEnabled": True,
                "standardFlowEnabled": False,
                "directAccessGrantsEnabled": True,
            }
            client_uuid = realm_admin.create_client(payload=payload)
        
        # Get Secret
        client_secrets_data = realm_admin.get_client_secrets(client_id=client_uuid)
        secret_value = client_secrets_data.get("value")
        
        return {
            "client_id": client_id,
            "client_secret": secret_value
        }

    def get_jwt_secret(self, realm_name: str) -> str:
        """
        Retrieves the HS256 logging secret/sig key if configured, 
        OR we might just use the client secret for HS256 if we configured the realm that way.
        
        By default Keycloak uses RS256. 
        Supabase often uses HS256 with a specific JWT secret.
        
        For now, let's assume we want to get the RS256 public key to validate, 
        OR we are forcing HS256.
        
        Simplification: We return a placeholder or the client secret if we treat it as the signing key for now.
        Use Case: PostgREST needs a JWT secret.
        """
        # TODO: Configure Realm to use HS256 and generate a secret or retrieve the RS256 public key.
        # For compatibility with PostgREST verifying RS256 validation is better but more complex setup.
        # Let's return a generated secret that we MIGHT force onto the realm or just a placeholder.
        
        # Placeholder
        return "super-secret-jwt-token-placeholder"
