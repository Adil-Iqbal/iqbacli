import typer
from . import size
from . import clear

app = typer.Typer(short_help="Review and manage file cache.")


app.add_typer(size.app, name="size")
app.add_typer(clear.app, name="clear")
