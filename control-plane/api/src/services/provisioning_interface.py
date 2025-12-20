from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class ProvisioningProvider(ABC):
    """Abstract base class for infrastructure provisioning providers."""

    @abstractmethod
    def provision_project(self, project_id: str, secrets: Optional[dict] = None) -> Dict[str, Any]:
        """Provision a new project infrastructure."""
        pass

    @abstractmethod
    def stop_project(self, project_id: str) -> None:
        """Stop a running project."""
        pass

    @abstractmethod
    def start_project(self, project_id: str) -> None:
        """Start a stopped project."""
        pass

    @abstractmethod
    def delete_project(self, project_id: str) -> None:
        """Delete a project and clean up resources."""
        pass

    @abstractmethod
    def restore_project(self, project_id: str) -> None:
        """Restore a deleted/archived project."""
        pass