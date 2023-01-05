import sys
from iqbacli import cli
from .logging import create_logger
from iqbacli.data.sql import initialize_database

logger = create_logger(__file__)


def main():
    logger.info(f"{sys.argv=}")
    initialize_database()
    cli.app()


if __name__ == "__main__":
    main()
