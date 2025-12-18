from pathlib import Path
from scripts.provision_project import provision_project as docker_provision


# Repo root → data-plane/projects
BASE_PROJECTS_DIR = (
    Path(__file__).resolve().parents[4] / "data-plane" / "projects"
)


def provision_project(project_id: str, secrets: dict):
    """
    Orchestrates provisioning of a project runtime.
    Delegates Docker + filesystem work to scripts layer.
    """
    BASE_PROJECTS_DIR.mkdir(parents=True, exist_ok=True)

    docker_provision(
        project_id=project_id,
        secrets=secrets,
        base_dir=BASE_PROJECTS_DIR,
    )
