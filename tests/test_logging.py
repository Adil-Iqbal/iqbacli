import sys
import logging
from iqbacli.logging import log_sys_argv


class FakeLogger:
    def __init__(self, name: str):
        self.name = name
        self.log_level = logging.NOTSET
        self.message = None

    def critical(self, message):
        self.log_level = logging.CRITICAL
        self.message = message


def test_log_sys_argv(monkeypatch):
    fake_logger = FakeLogger("test")
    monkeypatch.setattr(sys, "argv", [str(n) for n in range(5)])
    log_sys_argv(fake_logger)
    assert fake_logger.message == "SYS ARGV: iqba 1 2 3 4"
    assert fake_logger.log_level == logging.CRITICAL


def test_create_logger_prod():
    ...


def test_create_logger_dev():
    ...


def test_create_logger_dev_with_stream():
    ...


def test_create_logger_dev_different_log_levels():
    ...
