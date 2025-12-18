import subprocess
import shutil
from pathlib import Path

def get_project_dir(base_dir: Path, project_id: str) -> Path:
    return base_dir / project_id

def stop_project(project_id: str, base_dir: Path):
    """
    Stops the project containers.
    """
    project_dir = get_project_dir(base_dir, project_id)
    if not project_dir.exists():
        raise FileNotFoundError(f"Project {project_id} not found")

    compose_file = (
        Path(__file__).resolve().parents[1]
        / "data-plane"
        / "templates"
        / "docker-compose.project.yml"
    )

    subprocess.run(
        [
            "docker",
            "compose",
            "-f",
            str(compose_file),
            "--env-file",
            ".env",
            "down",
        ],
        cwd=project_dir,
        check=True,
    )

def start_project(project_id: str, base_dir: Path):
    """
    Starts the project containers.
    """
    project_dir = get_project_dir(base_dir, project_id)
    if not project_dir.exists():
        raise FileNotFoundError(f"Project {project_id} not found")
        
    compose_file = (
        Path(__file__).resolve().parents[1]
        / "data-plane"
        / "templates"
        / "docker-compose.project.yml"
    )

    subprocess.run(
        [
            "docker",
            "compose",
            "-f",
            str(compose_file),
            "--env-file",
            ".env",
            "up",
            "-d",
        ],
        cwd=project_dir,
        check=True,
    )

def delete_project(project_id: str, base_dir: Path):
    """
    Stops the project containers and soft-deletes (archives) the project directory.
    """
    project_dir = get_project_dir(base_dir, project_id)
    deleted_dir = base_dir / f"{project_id}_deleted"
    
    # 1. Stop and remove volumes
    if project_dir.exists():
        compose_file = (
            Path(__file__).resolve().parents[1]
            / "data-plane"
            / "templates"
            / "docker-compose.project.yml"
        )
        
        # Try to down, but don't fail if it fails
        try:
           subprocess.run(
                [
                    "docker",
                    "compose",
                    "-f",
                    str(compose_file),
                    "--env-file",
                    ".env",
                    "down",
                    # Note: Removing volumes (-v) might be dangerous for soft-delete if we want to restore data.
                    # For now, we will KEEP volumes to allow full restoration.
                ],
                cwd=project_dir,
                check=False,
            )
        except Exception as e:
            print(f"Warning: Failed to run docker compose down for {project_id}: {e}")

        # 2. Soft Delete: Rename directory
        if deleted_dir.exists():
            shutil.rmtree(deleted_dir) # Remove old archive if exists
            
        shutil.move(str(project_dir), str(deleted_dir))
    else:
         # Check if already deleted
         if not deleted_dir.exists():
             raise FileNotFoundError(f"Project {project_id} not found")

def restore_project(project_id: str, base_dir: Path):
    """
    Restores a soft-deleted project directory.
    """
    project_dir = get_project_dir(base_dir, project_id)
    deleted_dir = base_dir / f"{project_id}_deleted"

    if project_dir.exists():
        raise FileExistsError(f"Project {project_id} is already active")

    if not deleted_dir.exists():
         raise FileNotFoundError(f"Archived project {project_id} not found")
         
    # Restore directory
    shutil.move(str(deleted_dir), str(project_dir))
