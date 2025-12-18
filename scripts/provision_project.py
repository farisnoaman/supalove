import subprocess
from pathlib import Path


def provision_project(project_id: str, secrets: dict, base_dir: Path):
    """
    Creates project runtime directory, writes .env,
    and starts docker-compose for the project.
    """

    project_dir = base_dir / project_id
    project_dir.mkdir(parents=True, exist_ok=True)

    # 1️⃣ Write .env
    env_path = project_dir / ".env"

    env = {
        "PROJECT_ID": project_id,
        "DB_PASSWORD": secrets["DB_PASSWORD"],
        "JWT_SECRET": secrets["JWT_SECRET"],
        "DB_PORT": str(6000 + int(project_id[:2], 16)),
        "REST_PORT": str(7000 + int(project_id[:2], 16)),
    }

    with open(env_path, "w") as f:
        for k, v in env.items():
            f.write(f"{k}={v}\n")

    # 2️⃣ Run docker-compose inside project directory
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

    return env
