from ..paths import USER_DATA_DIR
from ..logging import create_logger

logger = create_logger(__file__)


def create_user_data():
    logger.info("Creating user data directory at {USER_DATA_DIR}")
    USER_DATA_DIR.parent.mkdir(exist_ok=True)
    USER_DATA_DIR.mkdir(exist_ok=True)
