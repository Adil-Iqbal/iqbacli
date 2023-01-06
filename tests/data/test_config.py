from pathlib import Path
from iqbacli.data.config import Config
from iqbacli.params import builtins


def test_create_new_config():
    test_config_path = Path(__file__).parent.resolve() / "config.json"
    try:
        assert not test_config_path.exists()
        config = Config.create_new_config(test_config_path)
        assert test_config_path.exists()
        assert config.cache == builtins.CACHE
        assert config.flat == builtins.FLAT
        assert config.regex == builtins.REGEX
    finally:
        test_config_path.unlink(missing_ok=True)


def test_config_to_dict():
    ...


def test_config_save():
    ...


def test_config_get():
    ...
