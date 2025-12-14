from enum import IntEnum
from typing import Optional

import typer
from rich.style import Style


class TaskPriority(IntEnum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2

    @staticmethod
    def validation_callback(value: Optional[int]) -> Optional[int]:
        """Validate priority value for CLI."""
        if value is None:
            return None
        if value not in [0, 1, 2]:
            raise typer.BadParameter("Only integers 0, 1, 2 are allowed.")
        return value

    @property
    def short_name(self) -> str:
        return f"P{str(self.value)}"

    @property
    def color(self) -> str:
        priority_colors = {
            TaskPriority.HIGH: "red",
            TaskPriority.MEDIUM: "yellow",
            TaskPriority.LOW: "magenta",
        }
        return priority_colors[self]

    @property
    def style(self) -> Style:
        return Style(color=self.color, bold=True)

    @property
    def display(self) -> str:
        return f"[{self.color}]{self.short_name}[/{self.color}]"


class TaskStatus(IntEnum):
    TODO = 0
    DONE = 1

    @staticmethod
    def validation_callback(value: Optional[int]) -> Optional[int]:
        if value is None:
            return None
        allowed_status = [0, 1]
        if value not in allowed_status:
            raise typer.BadParameter(f"Only status values {', '.join(map(str, allowed_status))} are allowed.")
        return value

    @property
    def color(self) -> str:
        return "red" if self == TaskStatus.TODO else "green"

    @property
    def emoji(self) -> str:
        return ":hourglass:" if self == TaskStatus.TODO else ":white_check_mark:"

    @property
    def style(self) -> Style:
        return Style(color=self.color, bold=True)

    @property
    def display(self) -> str:
        return f"{self.emoji} [{self.color}]{self.name}[/{self.color}]"
