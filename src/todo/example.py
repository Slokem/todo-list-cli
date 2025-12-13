import time

import typer
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.style import Style
from rich.table import Table
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True)

console = Console()


class VerboseHandler:
    def __init__(self, state: bool = False) -> None:
        self.state = state
        self.style = Style(color="yellow", bold=True)


vh = VerboseHandler()


@app.callback()
def main(verbose: bool = False) -> None:
    """
    A simple todo list CLI application.
    """
    vh.state = verbose
    if vh.state:
        console.print("Verbose mode is ON", style=vh.style)


@app.command("greet")
def greet_user(
    name: Annotated[str, typer.Argument(help="The first name of the user to greet")],
    last_name: Annotated[
        str, typer.Argument(help="The last name of the user to greet", rich_help_panel="Secondary Arguments")
    ] = "Doe",
    formal: Annotated[bool, typer.Option(help="Use a formal tone")] = False,
) -> None:
    """
    Greet a user. By Default will adopt a non formal tone.

    Use --formal flag to switch to a formal tone.
    Use --last-name to provide a last name.
    """
    if formal:
        if vh.state:
            console.print("Greeting user formally...", style=vh.style)
        print(Panel.fit(f"[bold blue]Good day[/bold blue] dear {name} {last_name}! :bow:", title="Formal Greeting"))
    else:
        if vh.state:
            console.print("Greeting user casually...", style=vh.style)
        print(Panel.fit(f"[bold green]Hi[/bold green] {name} {last_name}! :wave:", title="Casual Greeting"))


@app.command("farewell")
def bid_farewell_user(name: str, last_name: str = "", formal: bool = False) -> None:
    """
    Bid farewell to a user. By Default will adopt a non formal tone.

    Use --formal flag to switch to a formal tone.
    Use --last-name to provide a last name.
    """

    if formal:
        print(f"[bold blue]Goodbye[/bold blue] dear {name} {last_name}! :wave:")
    else:
        print(f"[bold green]Bye[/bold green] {name} {last_name}! :wave:")


@app.command()
def show() -> None:
    """
    Show the todo list.
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=False,
    ) as progress:
        progress.add_task(description=":inbox_tray: Collecting data...", total=None)
        time.sleep(2)
        progress.add_task(description=":art: Rendering...", total=None)
        time.sleep(2)
    table = Table("Task Description", "Priority", "Status")
    table.add_row("Finish interview notes", "P1", "TODO")
    table.add_row("Answer to fudosan", "P1", "TODO")
    console.print(table)


if __name__ == "__main__":
    app()
