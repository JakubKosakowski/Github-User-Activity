from typing import Optional, List

import typer

from app import __app_name__, __version__, api

app = typer.Typer()

def get_api_handler() -> api.APIHandler:
    return api.APIHandler()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.command()
def user(
    username: str = typer.Argument(...)
) -> List[str]:
    api_handler = get_api_handler()
    data = api_handler.get_user_info(username)
    typer.secho(data, fg=typer.colors.BLUE)

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return