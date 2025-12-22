import typer
from rich.console import Console
from pathlib import Path

app = typer.Typer()
console = Console()

@app.command()
def init(
    name: str = typer.Option(None, help="Project name"),
):
    """
    Initialize a new Supalove project in the current directory.
    """
    config_path = Path("supalove.toml")
    if config_path.exists():
        console.print("[yellow]supalove.toml already exists.[/yellow]")
        return
        
    project_name = name or Path.cwd().name
    
    content = f"""[project]
name = "{project_name}"
api_version = 1
"""
    with open(config_path, "w") as f:
        f.write(content)
        
    console.print(f"[green]Initialized Supalove project '{project_name}'[/green]")
    console.print("Created [bold]supalove.toml[/bold]")
