from ..paths import CONFIG_PATH


def get_path() -> str:
    return str(CONFIG_PATH.absolute())
