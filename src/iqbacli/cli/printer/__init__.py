from typing import Type
from rich.console import Console
from iqbacli.cli.printer.json_printer import JsonPrinter
from iqbacli.cli.printer.printer import Printer
from iqbacli.cli.printer.rich_printer import RichPrinter


_printer_dict: dict[tuple[bool], Type[Printer]] = {
    (False,): RichPrinter,
    (True,): JsonPrinter,
}


def printer_factory(_json: bool = False, no_color: bool = True) -> Printer:
    return _printer_dict[(_json,)](console=Console(), color=not no_color)
