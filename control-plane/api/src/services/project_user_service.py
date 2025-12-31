"""
Project User Service

Centralized service for managing users within project databases.
Handles user creation, deletion, and admin setup for new projects.
"""

import secrets
import string
import logging
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from models.user import User
from models.org_member import OrgMember, OrgRole
from models.project_secret import ProjectSecret
import requests

logger = logging.getLogger(__name__)


class ProjectUserService:
    """Service for managing users in project databases"""
    
    def __init__(self, control_plane_url: str = "http://localhost:8000"):
        self.control_plane_url = control_plane_url
    
    def generate_secure_password(self, length: int = 16) -> str:
        """
        Generate a cryptographically secure random password.
        
        Args:
            length: Length of password (default 16)
            
        Returns:
            Secure random password string with guaranteed length
        """
        # Ensure we have at least one of each required character type
        password_chars = [
            secrets.choice(string.ascii_uppercase),  # At least one uppercase
            secrets.choice(string.ascii_lowercase),  # At least one lowercase
            secrets.choice(string.digits),           # At least one digit
            secrets.choice("!@#$%^&*")              # At least one special char
        ]
        
        # Fill the rest with random characters
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        for _ in range(length - 4):
            password_chars.append(secrets.choice(alphabet))
        
        # Shuffle to avoid predictable pattern
        secrets.SystemRandom().shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def get_org_owner_email(self, db: Session, org_id: str) -> str:
        """
        Get the email of the organization owner.
        
        Args:
            db: Database session
            org_id: Organization ID
            
        Returns:
            Owner's email address
            
        Raises:
            ValueError: If no owner found
        """
        owner = db.query(User).join(OrgMember).filter(
            OrgMember.org_id == org_id,
            OrgMember.role == OrgRole.OWNER
        ).first()
        
        if not owner:
            raise ValueError(f"No owner found for organization {org_id}")
        
        return owner.email
    
    def create_user(
        self,
        project_id: str,
        email: str,
        password: str,
        role: str = "member",
        user_metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a user in the project's database via shared auth API.
        
        Args:
            project_id: Project ID
            email: User's email
            password: User's password
            role: User's role (admin or member)
            user_metadata: Optional additional user metadata
            
        Returns:
            User creation result from shared auth API
            
        Raises:
            Exception: If user creation fails
        """
        metadata = user_metadata or {}
        metadata["role"] = role
        
        try:
            # Call shared auth signup endpoint
            response = requests.post(
                f"{self.control_plane_url}/api/v1/projects/{project_id}/auth/v1/signup",
                json={
                    "email": email,
                    "password": password,
                    "data": metadata
                },
                timeout=30
            )
            
            if response.status_code != 200:
                error_detail = response.text
                logger.error(
                    f"Failed to create user in project {project_id}: "
                    f"Status {response.status_code}, Detail: {error_detail}"
                )
                raise Exception(f"Failed to create user: {error_detail}")
            
            result = response.json()
            logger.info(f"Successfully created user {email} in project {project_id}")
            return result
            
        except requests.RequestException as e:
            logger.error(f"Network error creating user in project {project_id}: {e}")
            raise Exception(f"Network error: {str(e)}")
    
    def create_admin_for_new_project(
        self,
        db: Session,
        project_id: str,
        org_id: str
    ) -> Dict[str, Any]:
        """
        Create an admin user for a newly created project.
        Uses the organization owner's email with an auto-generated password.
        
        Args:
            db: Database session
            project_id: Project ID
            org_id: Organization ID
            
        Returns:
            Dictionary with user info and temporary password
            
        Raises:
            ValueError: If org owner not found
            Exception: If user creation fails
        """
        logger.info(f"Creating admin user for project {project_id}")
        
        # Get organization owner's email
        owner_email = self.get_org_owner_email(db, org_id)
        
        # Generate secure temporary password
        temp_password = self.generate_secure_password()
        
        # Create admin user in project database
        try:
            result = self.create_user(
                project_id=project_id,
                email=owner_email,
                password=temp_password,
                role="admin",
                user_metadata={
                    "created_by": "system",
                    "is_project_admin": True,
                    "created_at_project_setup": True
                }
            )
            
            # Store temporary password in project secrets for one-time retrieval
            admin_pass_secret = ProjectSecret(
                project_id=project_id,
                key="ADMIN_TEMP_PASSWORD",
                value=temp_password
            )
            db.add(admin_pass_secret)
            db.commit()
            
            logger.info(
                f"Successfully created admin user {owner_email} "
                f"for project {project_id}"
            )
            
            return {
                **result,
                "temp_password": temp_password,
                "email": owner_email,
                "message": "Admin user created successfully"
            }
            
        except Exception as e:
            logger.error(
                f"Failed to create admin user for project {project_id}: {e}"
            )
            raise
