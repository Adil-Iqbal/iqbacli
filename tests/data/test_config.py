from pathlib import Path

import pytest

from iqbacli.data.config import Config
from iqbacli.params import builtins


@pytest.fixture
def config_path():
    return Path(__file__).parent.resolve() / "config.json"


@pytest.fixture
def sample_config(config_path):
    try:
        yield Config.create_new(config_path)
    finally:
        config_path.unlink(missing_ok=True)


def test_create_new_config(config_path):
    try:
        assert not config_path.exists()
        config = Config.create_new(config_path)
        assert config_path.exists()
        assert config.cache == builtins.CACHE
        assert config.flat == builtins.FLAT
        assert config.regex == builtins.REGEX
    finally:
        config_path.unlink(missing_ok=True)


def test_config_to_dict(sample_config: Config):
    config_dict = sample_config._to_dict()
    assert "cache" in config_dict
    assert "flat" in config_dict
    assert "regex" in config_dict
    assert config_dict["cache"] == sample_config.cache
    assert config_dict["flat"] == sample_config.flat
    assert config_dict["regex"] == sample_config.regex


def test_config_save(sample_config: Config, config_path: Path):
    sample_config.ignore_ext = "json"
    sample_config.save()
    reload_config = Config.get(config_path)
    assert reload_config.ignore_ext == "json"


def test_config_get(sample_config: Config, config_path: Path):
    reload_config = Config.get(config_path)
    assert sample_config.cache == reload_config.cache
    assert sample_config.flat == reload_config.flat
    assert sample_config.regex == reload_config.regex
