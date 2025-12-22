"""
GoTrue Proxy Service

Proxies requests to per-project GoTrue instances for user authentication management.
GoTrue runs on each project's AUTH_PORT and provides Supabase-compatible auth APIs.
"""

import httpx
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from models.project_secret import ProjectSecret


class GoTrueProxyService:
    """Proxy service to communicate with per-project GoTrue instances."""
    
    def __init__(self, db: Session, project_id: str):
        self.db = db
        self.project_id = project_id
        self._secrets: Dict[str, str] = {}
        self._load_secrets()
    
    def _load_secrets(self):
        """Load project secrets from database."""
        secrets = self.db.query(ProjectSecret).filter(
            ProjectSecret.project_id == self.project_id
        ).all()
        self._secrets = {s.key: s.value for s in secrets}
    
    @property
    def auth_url(self) -> str:
        """Get the GoTrue API URL for this project."""
        auth_port = self._secrets.get("AUTH_PORT", "9999")
        return f"http://localhost:{auth_port}"
    
    @property
    def service_role_key(self) -> str:
        """Get the service role key for admin operations."""
        return self._secrets.get("SERVICE_ROLE_KEY", "")
    
    def _get_admin_headers(self) -> Dict[str, str]:
        """Get headers for GoTrue admin API calls."""
        return {
            "Authorization": f"Bearer {self.service_role_key}",
            "Content-Type": "application/json",
            "apikey": self.service_role_key
        }
    
    async def list_users(self, page: int = 1, per_page: int = 50) -> List[Dict[str, Any]]:
        """
        List all users from GoTrue.
        Uses the admin endpoint: GET /admin/users
        """
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    f"{self.auth_url}/admin/users",
                    headers=self._get_admin_headers(),
                    params={"page": page, "per_page": per_page}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    # GoTrue returns { users: [...], aud: "..." }
                    users = data.get("users", [])
                    return self._transform_users(users)
                else:
                    print(f"GoTrue list_users error: {response.status_code} - {response.text}")
                    return []
        except httpx.ConnectError:
            print(f"GoTrue not reachable at {self.auth_url}")
            return []
        except Exception as e:
            print(f"GoTrue list_users exception: {e}")
            return []
    
    async def create_user(self, email: str, password: str, user_metadata: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
        """
        Create a new user in GoTrue.
        Uses the admin endpoint: POST /admin/users
        """
        try:
            payload = {
                "email": email,
                "password": password,
                "email_confirm": True,  # Auto-confirm for admin-created users
            }
            if user_metadata:
                payload["user_metadata"] = user_metadata
            
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.post(
                    f"{self.auth_url}/admin/users",
                    headers=self._get_admin_headers(),
                    json=payload
                )
                
                if response.status_code in [200, 201]:
                    user = response.json()
                    return self._transform_user(user)
                else:
                    print(f"GoTrue create_user error: {response.status_code} - {response.text}")
                    return None
        except httpx.ConnectError:
            print(f"GoTrue not reachable at {self.auth_url}")
            return None
        except Exception as e:
            print(f"GoTrue create_user exception: {e}")
            return None
    
    async def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific user by ID.
        Uses the admin endpoint: GET /admin/users/{id}
        """
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    f"{self.auth_url}/admin/users/{user_id}",
                    headers=self._get_admin_headers()
                )
                
                if response.status_code == 200:
                    user = response.json()
                    return self._transform_user(user)
                else:
                    return None
        except Exception as e:
            print(f"GoTrue get_user exception: {e}")
            return None
    
    async def update_user(self, user_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Update a user in GoTrue.
        Uses the admin endpoint: PUT /admin/users/{id}
        """
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.put(
                    f"{self.auth_url}/admin/users/{user_id}",
                    headers=self._get_admin_headers(),
                    json=data
                )
                
                if response.status_code == 200:
                    user = response.json()
                    return self._transform_user(user)
                else:
                    print(f"GoTrue update_user error: {response.status_code} - {response.text}")
                    return None
        except Exception as e:
            print(f"GoTrue update_user exception: {e}")
            return None
    
    async def delete_user(self, user_id: str) -> bool:
        """
        Delete a user from GoTrue.
        Uses the admin endpoint: DELETE /admin/users/{id}
        """
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.delete(
                    f"{self.auth_url}/admin/users/{user_id}",
                    headers=self._get_admin_headers()
                )
                
                return response.status_code in [200, 204]
        except Exception as e:
            print(f"GoTrue delete_user exception: {e}")
            return False
    
    async def check_health(self) -> bool:
        """Check if GoTrue is healthy."""
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self.auth_url}/health")
                return response.status_code == 200
        except:
            return False
    
    def _transform_users(self, users: List[Dict]) -> List[Dict[str, Any]]:
        """Transform GoTrue users to our format."""
        return [self._transform_user(u) for u in users]
    
    def _transform_user(self, user: Dict) -> Dict[str, Any]:
        """
        Transform GoTrue user to our expected format.
        
        GoTrue user format:
        {
            "id": "uuid",
            "email": "...",
            "created_at": "ISO8601",
            "email_confirmed_at": "...",
            "user_metadata": {...},
            ...
        }
        
        Our format:
        {
            "id": "uuid",
            "email": "...",
            "username": "...",
            "enabled": true,
            "createdTimestamp": 123456789
        }
        """
        from datetime import datetime
        
        created_at = user.get("created_at", "")
        try:
            dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            timestamp = int(dt.timestamp() * 1000)
        except:
            timestamp = 0
        
        return {
            "id": user.get("id", ""),
            "email": user.get("email", ""),
            "username": user.get("user_metadata", {}).get("username", user.get("email", "")),
            "enabled": user.get("email_confirmed_at") is not None,
            "createdTimestamp": timestamp
        }


# Synchronous wrapper functions for use in FastAPI endpoints
def get_gotrue_service(db: Session, project_id: str) -> GoTrueProxyService:
    """Factory function to create a GoTrueProxyService instance."""
    return GoTrueProxyService(db, project_id)
