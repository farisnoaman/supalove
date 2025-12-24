import os
import shutil
import subprocess
from pathlib import Path

def nuke_projects():
    # Define paths
    root_dir = Path(__file__).resolve().parent.parent
    projects_dir = root_dir / "data-plane" / "projects"

    if not projects_dir.exists():
        print("No projects directory found. Skipping project cleanup.")
        return

    print(f"Scanning for projects in {projects_dir}...")
    
    # Iterate over all project directories
    for project_dir in projects_dir.iterdir():
        if project_dir.is_dir() and (project_dir / "docker-compose.yml").exists():
            print(f"Found project: {project_dir.name}")
            print(f"  - Stopping containers...")
            try:
                subprocess.run(
                    ["docker", "compose", "down", "-v"],
                    cwd=project_dir,
                    check=True,
                    capture_output=True
                )
            except subprocess.CalledProcessError as e:
                print(f"  ! Failed to stop {project_dir.name}: {e}")
            
            print(f"  - Deleting directory...")
            shutil.rmtree(project_dir)
            print(f"  ✓ Deleted {project_dir.name}")

    print("All projects cleaned up.")

def nuke_control_plane():
    root_dir = Path(__file__).resolve().parent.parent
    print("Stopping Control Plane...")
    subprocess.run(["docker", "compose", "down", "-v"], cwd=root_dir, check=False)
    print("Control Plane stopped and volumes removed.")

if __name__ == "__main__":
    confirm = input("⚠️  WARNING: This will DELETE ALL PROJECTS and RESET the database. Type 'yes' to continue: ")
    if confirm.lower() == "yes":
        nuke_projects()
        nuke_control_plane()
        print("\n✅ System reset complete. Run './start_backend.sh' to restart.")
    else:
        print("Aborted.")
