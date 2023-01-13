import dotenv
from iqbacli import cli, driver
from .paths import log_paths
from .logging import create_logger, log_sys_argv


dotenv.load_dotenv()
logger = create_logger(__file__)


def main():
    try:
        log_sys_argv(logger)
        log_paths(logger)
        driver.init()
        cli.app()
    except Exception as exception:
        logger.exception(msg="Encountered an exception")
        raise exception


if __name__ == "__main__":
    main()
