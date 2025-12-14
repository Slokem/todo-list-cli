from rich.style import Style


class TaskPriority:
    priority_mapping = {
        0: {
            "name": "High",
            "color": "red",
        },
        1: {
            "name": "Medium",
            "color": "yellow",
        },
        2: {
            "name": "Low",
            "color": "magenta",
        },
    }

    def __init__(self, num: int) -> None:
        self.num: str = str(num)
        self.name: str = TaskPriority.priority_mapping[num]["name"]
        self.short_name: str = f"P{num}"
        self.color: str = TaskPriority.priority_mapping[num]["color"]
        self.display: str = f"[{self.color}]{self.short_name}[/{self.color}]"
        self.style: Style = Style(color=self.color, bold=True)


class TaskStatus:
    status_mapping = {
        0: {
            "name": "TODO",
            "color": "red",
            "emoji": ":hourglass:",
        },
        1: {
            "name": "DONE",
            "color": "green",
            "emoji": ":white_check_mark:",
        },
    }

    def __init__(self, num: int = 0) -> None:
        self.name: str = TaskStatus.status_mapping[num]["name"]
        self.style: Style = Style(color=TaskStatus.status_mapping[num]["color"], bold=True)
        self.emoji: str = TaskStatus.status_mapping[num]["emoji"]
        self.display: str = f"{self.emoji} [{self.style}]{self.name}[/{self.style}]"
