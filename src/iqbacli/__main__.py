from iqbacli import cli, driver
from iqbacli.paths import log_paths
from iqbacli.logging import create_logger, log_sys_argv
from iqbacli.params.env import log_env_vars


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
