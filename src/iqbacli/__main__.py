from iqbacli import cli
from .logging import create_logger, log_sys_argv
from iqbacli.data.sql import initialize_database

logger = create_logger(__file__)


def main():
    log_sys_argv(logger)
    initialize_database()
    cli.app()


if __name__ == "__main__":
    main()
