import os
import dotenv
import logging
from pathlib import Path
from logging import Logger, NullHandler, StreamHandler, Formatter

dotenv.load_dotenv()

BASE_DIR = Path(__file__).parent.resolve()


def create_logger(name: str) -> Logger:
    if os.getenv("IQBA_ENV") == "dev":
        dev_logger = logging.getLogger(name)
        dev_logger.setLevel(logging.INFO)
        dev_handler = StreamHandler()
        dev_formatter = Formatter(
            fmt="%(levelname)s | %(filename)s:%(lineno)d | %(asctime)s | %(message)s"
        )
        dev_handler.setFormatter(dev_formatter)
        dev_logger.addHandler(dev_handler)
        return dev_logger

    prod_handler = NullHandler()
    prod_logger = logging.getLogger(name)
    prod_logger.addHandler(prod_handler)
    return prod_logger
