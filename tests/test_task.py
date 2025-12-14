import pytest
from rich.style import Style

from todo.task import Task, TaskPriority, TaskStatus

##########################
# Tests for TaskPriority
##########################


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


@pytest.mark.parametrize(
    "value, expected_result",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (None, None),
    ],
    ids=["valid-0", "valid-1", "valid-2", "none"],
)
def test_task_priority_validation_callback_valid(value, expected_result):
    """Test TaskPriority validation callback with valid values."""
    assert TaskPriority.validation_callback(value) == expected_result


@pytest.mark.parametrize(
    "invalid_value",
    [3, -1, "high", ""],
    ids=["out-of-range-high", "out-of-range-low", "string", "empty-string"],
)
def test_task_priority_validation_callback_invalid(invalid_value):
    """Test TaskPriority validation callback with invalid values."""
    with pytest.raises(Exception):
        TaskPriority.validation_callback(invalid_value)


##########################
# Tests for TaskStatus
##########################


@pytest.mark.parametrize(
    "value, expected_result",
    [
        (0, 0),
        (1, 1),
        (None, None),
    ],
    ids=["valid-0", "valid-1", "none"],
)
def test_task_status_validation_callback_valid(value, expected_result):
    """Test TaskStatus validation callback with valid values."""
    assert TaskStatus.validation_callback(value) == expected_result


@pytest.mark.parametrize(
    "invalid_value",
    [2, -1, "todo", ""],
    ids=["out-of-range-high", "out-of-range-low", "string", "empty-string"],
)
def test_task_status_validation_callback_invalid(invalid_value):
    """Test TaskStatus validation callback with invalid values."""
    with pytest.raises(Exception):
        TaskStatus.validation_callback(invalid_value)


##################################
# Tests for Task model (SQL Model)
##################################


def test_task_model_creation():
    """Test Task model can be instantiated with required fields."""
    task = Task(description="Buy groceries", priority=0, status=0)

    assert task.description == "Buy groceries"
    assert task.priority == 0
    assert task.status == 0
    assert task.id is None  # Not set until saved to DB
    assert task.position is None
    assert task.created_at is None
    assert task.updated_at is None
    assert task.completed_at is None


def test_task_model_with_all_fields():
    """Test Task model with all fields populated."""
    task = Task(
        id=1,
        position=1,
        description="Complete project",
        priority=TaskPriority.HIGH,
        status=TaskStatus.TODO,
        created_at="2024-01-01T10:00:00",
        updated_at="2024-01-01T11:00:00",
        completed_at=None,
    )

    assert task.id == 1
    assert task.position == 1
    assert task.description == "Complete project"
    assert task.priority == 0  # TaskPriority.HIGH is 0
    assert task.status == 0  # TaskStatus.TODO is 0
    assert task.created_at == "2024-01-01T10:00:00"
    assert task.updated_at == "2024-01-01T11:00:00"
    assert task.completed_at is None


def test_task_model_default_status():
    """Test Task has default status of 0 (TODO)."""
    task = Task(description="Test task", priority=1)
    assert task.status == 0


@pytest.mark.parametrize(
    "priority, expected",
    [
        (0, TaskPriority.HIGH),
        (1, TaskPriority.MEDIUM),
        (2, TaskPriority.LOW),
    ],
    ids=["high", "medium", "low"],
)
def test_task_model_priority_values(priority, expected):
    """Test Task can be created with different priority values."""
    task = Task(description="Test", priority=priority)
    assert task.priority == priority
    assert TaskPriority(task.priority) == expected


@pytest.mark.parametrize(
    "status, expected",
    [
        (0, TaskStatus.TODO),
        (1, TaskStatus.DONE),
    ],
    ids=["todo", "done"],
)
def test_task_model_status_values(status, expected):
    """Test Task can be created with different status values."""
    task = Task(description="Test", priority=1, status=status)
    assert task.status == status
    assert TaskStatus(task.status) == expected
