import os
import sys
from iqbacli.paths import BASE_DIR
import logging
from iqbacli.logging import (
    _create_prod_logger,
    _create_dev_logger,
    log_sys_argv,
    create_logger,
)


def test_log_sys_argv(monkeypatch, caplog):
    caplog.clear()
    monkeypatch.setattr(sys, "argv", [str(n) for n in range(3)])
    log_sys_argv(logging.getLogger())
    assert caplog.record_tuples == [("root", logging.CRITICAL, "SYS ARGV: iqba 1 2")]


def test_create_prod_logger(caplog):
    caplog.clear()
    logger = logging.getLogger("foo")
    _create_prod_logger(logger)
    logger.info("bar")
    assert len(caplog.record_tuples) == 0


def test_create_dev_logger(caplog):
    caplog.clear()
    logger = logging.getLogger("foo")
    _create_dev_logger(logger)
    logger.info("foo")
    assert len(caplog.record_tuples) == 1


def test_create_logger_with_dev_env(caplog):
    try:
        caplog.clear()
        os.environ["IQBA_ENV"] = "dev"
        path = BASE_DIR / "foo.py"
        logger = create_logger(str(path.absolute()))
        logger.info("foo")
        assert len(caplog.record_tuples) == 1
    finally:
        if "IQBA_ENV" in os.environ:
            del os.environ["IQBA_ENV"]
