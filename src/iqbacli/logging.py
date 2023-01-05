import os
import dotenv
import logging
from pathlib import Path
from logging import Logger, NullHandler, StreamHandler, Formatter

dotenv.load_dotenv()

BASE_DIR = Path(__file__).parent.resolve()


def get_relative_path(filepathstr: str) -> str:
    filepath: Path = Path(filepathstr)
    relpath = filepath.relative_to(BASE_DIR)
    return str(relpath)


def create_logger(filepath: str) -> Logger:
    relpath = get_relative_path(filepath)
    if os.getenv("IQBA_ENV") == "dev":
        dev_logger = logging.getLogger(relpath)
        dev_logger.setLevel(logging.INFO)
        dev_handler = StreamHandler()
        dev_formatter = Formatter(
            fmt="%(levelname)s | %(name)s:%(lineno)d | %(asctime)s | %(message)s"
        )
        dev_handler.setFormatter(dev_formatter)
        dev_logger.addHandler(dev_handler)
        return dev_logger

    prod_handler = NullHandler()
    prod_logger = logging.getLogger(relpath)
    prod_logger.addHandler(prod_handler)
    return prod_logger
