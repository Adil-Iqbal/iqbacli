from __future__ import annotations

from rich.console import Console

from iqbacli.cli.printer.json_printer import JsonPrinter
from iqbacli.cli.printer.printer import Printer
from iqbacli.cli.printer.quiet_printer import QuietPrinter
from iqbacli.cli.printer.rich_printer import RichPrinter

__all__: list[str] = []


def printer_factory(
    quiet: bool = False, json: bool = False, no_color: bool = True
) -> Printer:
    console = Console()
    color = not no_color

    if quiet:
        return QuietPrinter(console=console, color=color)

    if json:
        return JsonPrinter(console=console, color=color)

    return RichPrinter(console=console, color=color)
