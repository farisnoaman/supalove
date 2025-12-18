from abc import ABC, abstractmethod
from typing import Dict, Any

class ProvisioningProvider(ABC):
    @abstractmethod
    def provision_project(self, project_id: str, secrets: dict = None) -> Dict[str, Any]:
        """
        Provisions a new project.
        Returns a dictionary containing connection details (e.g. api_url, db_url).
        """
        pass

    @abstractmethod
    def stop_project(self, project_id: str):
        """
        Stops the project's resources.
        """
        pass

    @abstractmethod
    def start_project(self, project_id: str):
        """
        Starts the project's resources.
        """
        pass

    @abstractmethod
    def delete_project(self, project_id: str):
        """
        Deletes (or soft-deletes) the project's resources.
        """
        pass

    @abstractmethod
    def restore_project(self, project_id: str):
        """
        Restores a deleted project.
        """
        pass
