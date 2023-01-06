import os
import sys
from typing import Final
import datetime
import dotenv
import logging
from pathlib import Path
from logging import FileHandler, Logger, NullHandler, StreamHandler, Formatter

dotenv.load_dotenv()

BASE_DIR: Final[Path] = Path(__file__).parent.resolve()
SRC_DIR: Final[Path] = BASE_DIR.parent.parent.resolve()
LOG_DIR: Final[Path] = SRC_DIR / "logs"


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


def _create_log_dir_if_needed() -> None:
    if LOG_DIR.exists() and LOG_DIR.is_dir():
        return
    LOG_DIR.mkdir()


def _resolve_log_level():
    if (env := os.getenv("IQBA_LOG_LEVEL")) is not None:
        return logging._nameToLevel[env.upper()]
    return logging.INFO


def _resolve_log_streaming(logger: Logger) -> None:
    if os.getenv("IQBA_STREAM_LOGS") == "1":
        stream_handler = StreamHandler()
        stream_handler.setFormatter(_DEFAULT_LOG_FORMATTER)
        logger.addHandler(stream_handler)


def _create_dev_logger(relpath: str) -> Logger:
    dev_logger = logging.getLogger(relpath)
    _create_log_dir_if_needed()

    dev_logger.setLevel(_resolve_log_level())
    dev_file_handler = FileHandler(LOG_FILE_PATH)
    dev_file_handler.setFormatter(_DEFAULT_LOG_FORMATTER)
    dev_logger.addHandler(dev_file_handler)
    _resolve_log_streaming(dev_logger)

    return dev_logger


def _create_prod_logger(relpath: str) -> Logger:
    prod_logger = logging.getLogger(relpath)
    prod_logger.addHandler(NullHandler())
    return prod_logger


def create_logger(filepath: str) -> Logger:
    relpath = _get_relative_path(filepath)
    if os.getenv("IQBA_ENV") == "dev":
        return _create_dev_logger(relpath)
    return _create_prod_logger(relpath)


def log_sys_argv(logger: Logger) -> None:
    logger.critical(f"SYS ARGV: iqba {' '.join(sys.argv[1:])}")
