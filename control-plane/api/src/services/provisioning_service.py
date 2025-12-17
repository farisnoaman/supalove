import subprocess
from pathlib import Path

BASE_PROJECTS_DIR = Path("/tmp/supabase-projects")
TEMPLATE_DIR = Path(__file__).resolve().parents[4] / "data-plane/project-template"


def provision_project(project_id: str):
    project_dir = BASE_PROJECTS_DIR / project_id
    project_dir.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        ["cp", "-r", str(TEMPLATE_DIR) + "/.", str(project_dir)],
        check=True
    )

    # subprocess.run(
    #     ["docker", "compose", "up", "-d"],
    #     cwd=project_dir,
    #     check=True
    # )
