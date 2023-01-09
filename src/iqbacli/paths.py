import os
from logging import Logger
from platformdirs import PlatformDirs
from pathlib import Path
from typing import Any, Final

# Internal Paths
BASE_DIR: Final[Path] = Path(__file__).parent.resolve()
ROOT_DIR: Final[Path] = BASE_DIR.parent.parent.resolve()
SQL_DIR = BASE_DIR / "data" / "sql"

# User Paths
APP_DIRS: Final[Any] = PlatformDirs(appname="iqbacli")
USER_DATA_DIR: Final[Path] = Path(APP_DIRS.user_data_dir)


def _resolve_log_dir() -> Path:
    if "IQBA_ENV" in os.environ and os.getenv("IQBA_ENV") == "dev":
        return ROOT_DIR / "logs"
    return USER_DATA_DIR / "logs"


CONFIG_PATH: Final[Path] = Path(APP_DIRS.user_config_dir) / "iqbaconfig.json"
DB_PATH: Final[Path] = USER_DATA_DIR / "database.sqlite3"
LOG_DIR: Final[Path] = _resolve_log_dir()


# Log all paths in file.
def log_paths(logger: Logger) -> None:
    for key, path in globals().items():
        if isinstance(path, Path):
            logger.info(f"Initializing with {key}={path}")
