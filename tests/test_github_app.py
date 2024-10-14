import pytest

from typer.testing import CliRunner

from app import __app_name__, __version__, cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ['--version'])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}" in result.stdout

test_data1 = {
    "username": 'JakubKosakowski'
}

@pytest.mark.parametrize(
    "username, expected_public_repos, expected_followers",
    [
        pytest.param(
            test_data1['username'],
            15,
            3
        )
    ]
)
def test_user(username: str, expected_public_repos: int, expected_followers: int):
    api_handler = cli.get_api_handler()
    user = api_handler.get_user_info(username)
    assert user['public_repos'] == expected_public_repos
    assert user['followers'] == expected_followers
