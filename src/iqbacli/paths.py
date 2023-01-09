from __future__ import annotations

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
CONFIG_PATH: Final[Path] = Path(APP_DIRS.user_config_dir) / "iqbaconfig.json"
DB_PATH: Final[Path] = USER_DATA_DIR / "database.sqlite3"
_log_paths: dict[str, Path] = {"dev": ROOT_DIR, "prod": USER_DATA_DIR}
LOG_DIR: Final[Path] = _log_paths[os.getenv("IQBA_ENV", "prod")] / "logs"


# Log all paths in file.
def log_paths(logger: Logger) -> None:
    for key, path in globals().items():
        if isinstance(path, Path):
            logger.info(f"Initializing with {key}={path}")
