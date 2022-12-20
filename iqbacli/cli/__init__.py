import typer
from . import search
from . import history
from . import config
from . import cache
from . import result

main = typer.Typer()

main.add_typer(search.app, name="search")
main.add_typer(history.app, name="history")
main.add_typer(config.app, name="config")
main.add_typer(cache.app, name="cache")
main.add_typer(result.app, name="result")
