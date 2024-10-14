from typing import Optional, Dict, List, Any

import typer

from app import __app_name__, __version__, api, EVENTS, ERRORS

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
) -> None:
    api_handler = get_api_handler()
    data, error = api_handler.get_user_info(username)
    if error:
        typer.secho(f'Searching user data failed with "{ERRORS[error]}"',
                    fg=typer.colors.RED)
        raise typer.Exit(1)
    else:
        typer.secho(data, fg=typer.colors.BLUE)

@app.command()
def events(
    username: str = typer.Argument(...)
) -> None:
    api_handler = get_api_handler()
    data, error = api_handler.get_user_events(username)
    for event in data:
        info = f"""({event['created_at']}) #{event['id']} - """
        event_info = EVENTS[event['type']]
        if event['type'] == 'PushEvent':
            event_info = event_info.replace('{AoC}', str(event['payload']['size'])).replace('{repo_name}', event['repo']['name'])
        typer.secho(f"{info} {event_info}\n",
                    fg=typer.colors.BLUE)

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