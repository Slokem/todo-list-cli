from enum import IntEnum

from rich.style import Style


class TaskPriority(IntEnum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2

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
