import uuid
from services.provisioning_service import provision_project


def create_project():
    project_id = uuid.uuid4().hex[:12]

    provision_project(project_id)

    return {
        "project_id": project_id,
        "status": "running",
        "api_url": f"http://localhost:{project_id}"
    }
