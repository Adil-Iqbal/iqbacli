from ..paths import USER_DATA_DIR
from ..logging import create_logger

logger = create_logger(__file__)


def create_user_data():
    if USER_DATA_DIR.exists():
        return

    logger.info("Creating user data directory at {USER_DATA_DIR}")
    if not USER_DATA_DIR.parent.exists():
        USER_DATA_DIR.parent.mkdir()
    USER_DATA_DIR.mkdir()
