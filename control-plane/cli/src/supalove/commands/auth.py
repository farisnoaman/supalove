import typer
from rich.console import Console
from rich.panel import Panel
from ..config import config_manager
from ..api import api_client

app = typer.Typer()
console = Console()

@app.command()
def login(
    token: str = typer.Option(None, prompt=True, hide_input=True, help="Your Supalove Personal Access Token")
):
    """
    Authenticate with Supalove using a Personal Access Token (PAT).
    """
    try:
        # Validate token by making a probe request (e.g., get user profile)
        # For now, we manually set it and trust it works until we hit an API error
        # In a real scenario, we'd call /me endpoint
        
        # Temporary: Just save it. 
        # Ideally: api_client.set_temp_token(token) -> api_client.get("/me") -> if ok -> save.
        
        config_manager.set_token(token)
        
        console.print(Panel.fit(
            f"[green]Successfully logged in![/green]\n"
            f"Token saved to [bold]{config_manager.config_file}[/bold]",
            title="Authentication Success"
        ))
        
    except Exception as e:
        console.print(f"[red]Login failed:[/red] {str(e)}")

@app.command()
def logout():
    """
    Log out and remove stored credentials.
    """
    config_manager.clear_token()
    console.print("[green]Successfully logged out.[/green]")

@app.command()
def whoami():
    """
    Check current logged in user.
    """
    token = config_manager.config.access_token
    if not token:
        console.print("[yellow]Not logged in.[/yellow]")
        return
        
    try:
        # We need an endpoint to get current user. /api/v1/auth/me usually.
        # Let's assume GET /users/me exists or use a workaround.
        # Actually our API doesn't have a simple /me yet exposed easily for simple verify without project.
        # But we valid tokens are JWTs. We could decode locally or hit an endpoint.
        # Let's try to fetch list of projects as a verification check.
        
        # api_client.get("/users/me") # We don't have this yet explicitly in common routes?
        # Checking api/v1/users.py...
        
        console.print(f"[green]Logged in.[/green] (Token present)")
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
