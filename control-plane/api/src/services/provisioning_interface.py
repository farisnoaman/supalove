from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class Provisioner(ABC):
    """Abstract base class for infrastructure provisioning providers."""

    @abstractmethod
    def provision(self, project_id: str, secrets: Optional[dict] = None, custom_domain: Optional[str] = None) -> Dict[str, Any]:
        """Provision a new project infrastructure."""
        pass

    @abstractmethod
    def destroy(self, project_id: str) -> None:
        """Delete a project and clean up resources."""
        pass

    @abstractmethod
    def stop(self, project_id: str) -> None:
        """Stop a running project."""
        pass

    @abstractmethod
    def start(self, project_id: str) -> None:
        """Start a stopped project."""
        pass

    @abstractmethod
    def restore(self, project_id: str) -> None:
        """Restore a deleted/archived project."""
        pass