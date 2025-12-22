import typer
from rich.console import Console
from .commands import auth, projects, deploy, init
from .config import config_manager

app = typer.Typer(
    name="supalove",
    help="CLI for managing Supalove projects and switching between development and production.",
    no_args_is_help=True
)

console = Console()

app.add_typer(auth.app, name="auth", help="Login, logout, and manage sessions.")
app.add_typer(projects.app, name="projects", help="Manage projects (create, list, link).")
app.add_typer(deploy.app, name="deploy", help="Deploy resources (functions, assets).")
app.add_typer(init.app, name="init", help="Initialize a new project.")

# Global callback options
@app.callback()
def main(
    api_url: str = typer.Option(None, help="Override API URL"),
):
    if api_url:
        config_manager.config.api_url = api_url

if __name__ == "__main__":
    app()
