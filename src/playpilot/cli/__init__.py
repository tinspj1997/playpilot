import typer

app = typer.Typer(help="PlayPilot - Test automation tool", no_args_is_help=True)


@app.command()
def run(
    url: str = typer.Option(..., help="Target URL to test"),
    config: str = typer.Option(..., "--config", "-c", help="Test configuration or data"),
) -> None:
    """Run tests or automation against a target URL."""
    typer.echo(f"Running playpilot with URL: {url}")
    typer.echo(f"Config/Data: {config}")


__all__ = ["app"]
