import pytest
from rich.style import Style

from todo.task import TaskPriority, TaskStatus


@pytest.mark.parametrize(
    "priority, expected_value, expected_name, expected_color, expected_short_name",
    [
        (TaskPriority.HIGH, 0, "HIGH", "red", "P0"),
        (TaskPriority.MEDIUM, 1, "MEDIUM", "yellow", "P1"),
        (TaskPriority.LOW, 2, "LOW", "magenta", "P2"),
    ],
    ids=["high", "medium", "low"],
)
def test_task_priority_enum_properties(priority, expected_value, expected_name, expected_color, expected_short_name):
    """Test TaskPriority enum members and their properties."""
    assert priority == expected_value
    assert priority.name == expected_name
    assert priority.short_name == expected_short_name
    assert priority.color == expected_color
    assert isinstance(priority.style, Style)
    assert priority.style.color.name == expected_color
    assert priority.style.bold
    assert priority.display == f"[{expected_color}]{expected_short_name}[/{expected_color}]"


@pytest.mark.parametrize(
    "status, expected_value, expected_name, expected_color, expected_emoji",
    [
        (TaskStatus.TODO, 0, "TODO", "red", ":hourglass:"),
        (TaskStatus.DONE, 1, "DONE", "green", ":white_check_mark:"),
    ],
    ids=["todo", "done"],
)
def test_task_status_enum_properties(status, expected_value, expected_name, expected_color, expected_emoji):
    """Test TaskStatus enum members and their properties."""
    assert status == expected_value
    assert status.name == expected_name
    assert status.color == expected_color
    assert status.emoji == expected_emoji
    assert isinstance(status.style, Style)
    assert status.style.color.name == expected_color
    assert status.style.bold
    assert status.display == f"{expected_emoji} [{expected_color}]{expected_name}[/{expected_color}]"
