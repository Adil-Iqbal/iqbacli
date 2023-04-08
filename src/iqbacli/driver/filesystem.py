from __future__ import annotations

from ..logging import create_logger
from ..paths import USER_DATA_DIR

logger = create_logger(__file__)


def create_user_data():
    if not USER_DATA_DIR.exists():
        logger.info(f"Creating user data directory at {USER_DATA_DIR=}")
    USER_DATA_DIR.parent.mkdir(exist_ok=True)
    USER_DATA_DIR.mkdir(exist_ok=True)
