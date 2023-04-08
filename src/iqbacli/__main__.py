from __future__ import annotations

from iqbacli import cli
from iqbacli import driver
from iqbacli.logging import create_logger
from iqbacli.logging import log_sys_argv
from iqbacli.params.env import log_env_vars
from iqbacli.paths import log_paths

logger = create_logger(__file__)


def main():
    log_sys_argv(logger)
    log_env_vars(logger)
    log_paths(logger)

    try:
        driver.init()
        cli.app()
    except Exception as exception:
        logger.exception(msg="Encountered an exception")
        raise exception


if __name__ == "__main__":
    main()
