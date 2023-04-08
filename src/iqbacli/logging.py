from __future__ import annotations

import datetime
import logging
import sys
from logging import FileHandler
from logging import Formatter
from logging import Logger
from logging import NullHandler
from logging import StreamHandler
from pathlib import Path
from typing import Final

from iqbacli.params.env import get_env
from iqbacli.params.env import is_env
from iqbacli.paths import BASE_DIR
from iqbacli.paths import LOG_DIR


def _create_log_file_path() -> str:
    now: str = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
    filepath: Path = LOG_DIR / f"iqba_{now}.log"
    return str(filepath.absolute())


LOG_FILE_PATH: Final[str] = _create_log_file_path()
_DEFAULT_LOG_FORMATTER: Final[Formatter] = Formatter(
    fmt="%(asctime)s.%(msecs)03d | %(levelname)s | %(name)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d,%H:%M:%S",
)


def _get_relative_path(filepathstr: str) -> str:
    filepath: Path = Path(filepathstr)
    relpath = filepath.relative_to(BASE_DIR)
    return str(relpath)


def _resolve_log_level():
    if (env := get_env("LOG_LEVEL")) is not None:
        return logging._nameToLevel[env.upper()]
    return logging.INFO


def _resolve_log_streaming(logger: Logger) -> None:
    if is_env("STREAM_LOGS", "1"):
        stream_handler = StreamHandler()
        stream_handler.setFormatter(_DEFAULT_LOG_FORMATTER)
        logger.addHandler(stream_handler)


def _create_dev_logger(dev_logger: Logger) -> Logger:
    LOG_DIR.mkdir(exist_ok=True)
    dev_logger.setLevel(_resolve_log_level())
    dev_file_handler = FileHandler(LOG_FILE_PATH)
    dev_file_handler.setFormatter(_DEFAULT_LOG_FORMATTER)
    dev_logger.addHandler(dev_file_handler)
    _resolve_log_streaming(dev_logger)

    return dev_logger


def _create_prod_logger(prod_logger: Logger) -> Logger:
    prod_logger.addHandler(NullHandler())
    return prod_logger


def create_logger(filepath: str) -> Logger:
    relpath = _get_relative_path(filepath)
    logger = logging.getLogger(relpath)
    if is_env("ENV", "dev"):
        return _create_dev_logger(logger)
    return _create_prod_logger(logger)


def log_sys_argv(logger: Logger) -> None:
    logger.critical(f"SYS ARGV: iqba {' '.join(sys.argv[1:])}")
