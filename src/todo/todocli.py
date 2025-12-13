from typing import Optional

import typer
from rich.console import Console
from rich.style import Style
from rich.table import Table
from typing_extensions import Annotated

console = Console()

app = typer.Typer(no_args_is_help=True)


@app.callback()
def main() -> None:
    """
    A simple todo list CLI application.
    """
    pass


def priority_callback(value: int) -> int:
    if value not in [0, 1, 2]:
        raise typer.BadParameter("Only integers 0, 1, 2 are allowed.")
    return value


def status_callback(value: str) -> str:
    allowed_status = ["TODO", "DONE"]
    if value not in allowed_status:
        raise typer.BadParameter(f"Only status values {', '.join(allowed_status)} are allowed.")
    return value


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
            "color": "",
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
        "TODO": {"color": "red", "emoji": ":hourglass:"},
        "DONE": {"color": "green", "emoji": ":white_check_mark:"},
    }

    def __init__(self, name: str = "TODO") -> None:
        self.name: str = name
        self.style: Style = Style(color=TaskStatus.status_mapping[name]["color"], bold=True)
        self.emoji: str = TaskStatus.status_mapping[name]["emoji"]
        self.display: str = f"{self.emoji} [{self.style}]{self.name}[/{self.style}]"


@app.command("add")
def add_task(
    task: Annotated[str, typer.Argument(help="Description of the task to add")],
    priority: Annotated[
        int,
        typer.Option(
            "--priority",
            "-p",
            help="[ 0 | 1 | 2 ] Priority of the task corresponding to P0=High, P1=Medium, P2=Low",
            callback=priority_callback,
            show_default=True,
        ),
    ] = 2,
) -> None:
    """
    Add a new task to the todo list.
    """
    p = TaskPriority(priority)
    console.print(
        f":heavy_plus_sign: [green]Adding[/green] task '{task}' with priority {p.short_name}={p.name} and status {TaskStatus().name}."
    )
    pass


@app.command("del")
def delete_task(id: Annotated[int, typer.Argument(help="ID of the task to delete")]) -> None:
    """
    Delete a task from the todo list by its ID.
    """
    console.print(f":broom: [red]Deleting[/red] task with ID {id}.")
    pass


@app.command("update")
def update_task(
    id: Annotated[int, typer.Argument(help="ID of the task to update")],
    status: Annotated[
        Optional[str],
        typer.Option(
            "--status",
            "-s",
            help="New status of the task",
        ),
    ] = None,
    task: Annotated[Optional[str], typer.Option("--task", "-t", help="New description for the task")] = None,
    priority: Annotated[
        Optional[int],
        typer.Option(
            "--priority",
            "-p",
            help="[ 0 | 1 | 2 ] New priority of the task corresponding to P0=High, P1=Medium, P2=Low",
        ),
    ] = None,
) -> None:
    """
    Update a task's description and/or priority and/or status by its ID.
    """
    message = f":pencil: [yellow]Updating[/yellow] task with ID {str(id)}"
    message = message + "\n    with new description: " + f"{task}" if task else message
    message = (
        message + "\n    with new priority: " + f"{TaskPriority(priority).short_name}"
        if priority is not None
        else message
    )
    message = message + "\n    with new status: " + f"{status}" if status else message
    console.print(f"{message}")
    pass


@app.command("show")
def show() -> None:
    """
    Show the todo list.
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Task ID", justify="right", style="cyan", no_wrap=True, width=6)
    table.add_column("Description", justify="left", no_wrap=False, max_width=40)
    table.add_column("Priority", justify="center")
    table.add_column("Status", justify="center")
    table.add_row("1", "Finish interview notes", TaskPriority(0).display, TaskStatus("DONE").display)
    table.add_row("2", "Answer to fudosan", TaskPriority(1).display, TaskStatus("TODO").display)
    console.print(table)


if __name__ == "__main__":
    app()
