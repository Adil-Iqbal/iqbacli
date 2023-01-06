import sys
import logging
from iqbacli.logging import _create_prod_logger, log_sys_argv


def test_log_sys_argv(monkeypatch, caplog):
    caplog.clear()
    monkeypatch.setattr(sys, "argv", [str(n) for n in range(3)])
    log_sys_argv(logging.getLogger())
    assert caplog.record_tuples == [("root", logging.CRITICAL, "SYS ARGV: iqba 1 2")]


def test_create_logger_prod(caplog):
    caplog.clear()
    logger = _create_prod_logger("foo")
    logger.info("bar")
    assert len(caplog.record_tuples) == 0
