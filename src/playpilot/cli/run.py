import typer
import asyncio
from playpilot.tools.source import fetch_page_source

app = typer.Typer(help="Run tests or automation")


@app.callback(invoke_without_command=True)
def main(
    url: str = typer.Option(..., help="Target URL to test"),
) -> None:
    """Run tests or automation against a target URL."""
    typer.echo(f"Running playpilot with URL: {url}")

    # Fetch the page source
    typer.echo("Fetching page source...")
    html = asyncio.run(fetch_page_source(url))
    if html:
        typer.echo("Page source fetched successfully.")
    else:
        typer.echo("Failed to fetch page source.")
