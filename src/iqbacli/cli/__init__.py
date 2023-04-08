import typer

from . import cache, config, history, result, search

app = typer.Typer()

app.add_typer(search.app, name="search")
app.add_typer(history.app, name="history")
app.add_typer(config.app, name="config")
app.add_typer(cache.app, name="cache")
app.add_typer(result.app, name="result")
