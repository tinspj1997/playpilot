import typer
from playpilot.cli import run

app = typer.Typer(help="PlayPilot - Test automation tool", no_args_is_help=True)
app.add_typer(run.app, name="run")

__all__ = ["app"]
