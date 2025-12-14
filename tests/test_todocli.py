import pytest
from typer.testing import CliRunner

from todo.todocli import app

runner = CliRunner()


@pytest.mark.parametrize(
    "args, expected_exit_code",
    [
        (["--help"], 0),
        (["add"], 2),  # No Argument Provided
        (["add", "Buy groceries"], 0),  # Only Task Description Provided
        (["add", "Buy groceries", "And do more"], 2),  # Too Many Arguments Provided
        (["add", "Buy groceries", "--priority", "0"], 0),  # Valid Priority
        (["add", "Buy groceries", "--priority", "1"], 0),  # Valid Priority
        (["add", "Buy groceries", "--priority", "2"], 0),  # Valid Priority
        (["add", "Buy groceries", "--priority", "3"], 2),  # Invalid Priority (value out of range)
        (["add", "Buy groceries", "--priority", "high"], 2),  # Invalid Priority (type)
    ],
)
def test_todo_add(args: list[str], expected_exit_code: int) -> None:
    """
    Test exit code of the 'add' command of the todo CLI application on various inputs.
    """

    result = runner.invoke(app, args)
    assert result.exit_code == expected_exit_code


@pytest.mark.parametrize(
    "args, expected_exit_code",
    [
        (["--help"], 0),
        (["del"], 2),
        (["del", "1"], 0),
        (["del", "abc"], 2),
    ],
)
def test_todo_del(args: list[str], expected_exit_code: int) -> None:
    """
    Test exit code of the 'del' command of the todo CLI application on various inputs.
    """

    result = runner.invoke(app, args)
    assert result.exit_code == expected_exit_code


@pytest.mark.parametrize(
    "args, expected_exit_code",
    [
        (["--help"], 0),
        (["update"], 2),
        (["update", "1"], 0),
        (["update", "abc"], 2),
        (["update", "1", "more"], 2),
        (["update", "1", "--priority"], 2),
        (["update", "1", "--priority", ""], 2),
        (["update", "1", "--priority", "0"], 0),
        (["update", "1", "--priority", "1"], 0),
        (["update", "1", "--priority", "2"], 0),
        (["update", "1", "--priority", "3"], 2),
        (["update", "1", "--priority", "abc"], 2),
        (["update", "1", "--task", ""], 0),
        (["update", "1", "--task", "Updated task"], 0),
        (["update", "1", "--status"], 2),
        (["update", "1", "--status"], 2),
        (["update", "1", "--status", "0"], 0),
        (["update", "1", "--status", "1"], 0),
        (["update", "1", "--status", "2"], 2),
        (["update", "1", "--status", "abc"], 2),
        (["update", "1", "--status", "1", "--priority", "0", "--task", "Updated task"], 0),
    ],
)
def test_todo_update(args: list[str], expected_exit_code: int) -> None:
    """
    Test exit code of the 'update' command of the todo CLI application on various inputs.
    """

    result = runner.invoke(app, args)
    assert result.exit_code == expected_exit_code


@pytest.mark.parametrize(
    "args, expected_exit_code",
    [
        (["--help"], 0),
        (["show"], 0),
    ],
)
def test_todo_show(args: list[str], expected_exit_code: int) -> None:
    """
    Test exit code of the 'show' command of the todo CLI application on various inputs.
    """

    result = runner.invoke(app, args)
    assert result.exit_code == expected_exit_code
