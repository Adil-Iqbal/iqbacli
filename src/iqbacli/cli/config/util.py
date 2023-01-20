import humps
from rich.console import Console
from rich.table import Table
from ...driver import config
from ...paths import CONFIG_PATH
from pathlib import Path


def print_config_table(
    config_path: Path = CONFIG_PATH, console: Console = Console()
) -> None:
    config_dict = config.get_config_dict(config_path)
    table = Table(title="User Configuration")
    table.add_column("Name")
    table.add_column("Value")

    for key, value in config_dict.items():
        table.add_row(humps.kebabize(key), str(value))

    console.print(table)
