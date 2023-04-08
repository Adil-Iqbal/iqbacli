import typer

from . import get, path, reset, set, set_file

app = typer.Typer(short_help="Review and change configuration.")


app.add_typer(get.app, name="get")
app.add_typer(reset.app, name="reset")
app.add_typer(set.app, name="set")
app.add_typer(set_file.app, name="set-file")
app.add_typer(path.app, name="path")
