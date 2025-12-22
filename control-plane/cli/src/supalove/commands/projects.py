import typer
from rich.console import Console
from rich.table import Table
from ..api import api_client
from ..config import config_manager

app = typer.Typer()
console = Console()

@app.command("list")
def list_projects():
    """
    List all projects in your organization.
    """
    try:
        # We assume the user has access to at least one Org. 
        # Ideally we list Orgs first, but for MVP let's assume single org context or fetch all.
        # API: /api/v1/orgs/{id}/projects
        
        # Phase 6 limitation: CLI doesn't know Org ID unless we save it or fetch "my orgs"
        # Let's add `supalove orgs list` eventually.
        # For now, let's ask for Org ID or try to infer.
        
        # MVP Hack: Since we don't have a "get all my projects across orgs" endpoint yet,
        # we might need to prompt for Org ID.
        pass 
        console.print("[yellow]Listing projects requires Organization ID context. Feature coming soon.[/yellow]")
        
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")

@app.command("create")
def create_project(
    name: str = typer.Option(..., prompt="Project Name"),
    org_id: str = typer.Option(..., prompt="Organization ID"),
    plan: str = typer.Option("free", help="Subscription plan (free/pro)")
):
    """
    Create a new project in an organization.
    """
    try:
        payload = {
            "name": name,
            "org_id": org_id
        }
        
        resp = api_client.post("/api/v1/projects", data=payload)
        console.print(f"[green]Project '{resp['name']}' created successfully![/green] (ID: {resp['id']})")
        
    except Exception as e:
        console.print(f"[red]Failed to create project:[/red] {str(e)}")
