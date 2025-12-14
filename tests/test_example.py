import pytest
from typer.testing import CliRunner

from todo.example import app

runner = CliRunner()


@pytest.mark.parametrize(
    "args, expected_exit_code, expected_output",
    [
        (["--help"], 0, "A simple todo list CLI application."),
        (["greet", "Alice"], 0, "Hi Alice Doe!"),
        (["greet", "Bob", "--formal"], 0, "Good day dear Bob Doe!"),
        (["greet", "Bob", "Smith", "--formal"], 0, "Good day dear Bob Smith!"),
    ],
)
def test_app_cmd_greet(args: list[str], expected_exit_code: int, expected_output: str) -> None:
    result = runner.invoke(app, args)
    assert result.exit_code == expected_exit_code
    assert expected_output in result.output


@pytest.mark.parametrize(
    "args, expected_exit_code, expected_output",
    [
        (["--help"], 0, "A simple todo list CLI application."),
        (["farewell", "Alice"], 0, "Bye Alice !"),
        (["farewell", "Bob", "--formal"], 0, "Goodbye dear Bob !"),
        (["farewell", "Bob", "--last-name", "Smith", "--formal"], 0, "Goodbye dear Bob Smith!"),
        (["farewell", "Bob", "Smith", "--formal"], 2, "Got unexpected extra argument"),
    ],
)
def test_app_cmd_farewell(args: list[str], expected_exit_code: int, expected_output: str) -> None:
    result = runner.invoke(app, args)
    assert result.exit_code == expected_exit_code
    assert expected_output in result.output
