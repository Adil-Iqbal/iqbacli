import typer

from . import clear, delete, get, last, list, undo

app = typer.Typer(short_help="Review and operate on previous search queries.")


app.add_typer(list.app, name="list")
app.add_typer(undo.app, name="undo")
app.add_typer(clear.app, name="clear")
app.add_typer(get.app, name="get")
app.add_typer(delete.app, name="delete")
app.add_typer(last.app, name="last")
