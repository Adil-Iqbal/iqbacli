from __future__ import annotations

import typer

from . import clear
from . import size

app = typer.Typer(short_help="Review and manage file cache.")


app.add_typer(size.app, name="size")
app.add_typer(clear.app, name="clear")
