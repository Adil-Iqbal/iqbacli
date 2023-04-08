import typer

from . import delete, get, last, list, show

app = typer.Typer(short_help="Review and operate on obtained search results.")


app.add_typer(list.app, name="list")
app.add_typer(show.app, name="show")
app.add_typer(get.app, name="get")
app.add_typer(delete.app, name="delete")
app.add_typer(last.app, name="last")
