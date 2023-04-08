from __future__ import annotations

import os
from logging import Logger
from typing import Optional
from typing import Sequence

import dotenv

dotenv.load_dotenv()

_envvars: Sequence[str] = ["ENV", "LOG_LEVEL", "STREAM_LOGS", "SUGGESTIONS"]


def get_env(envvar: str, default: Optional[str] = None) -> Optional[str]:
    if not envvar.startswith("IQBA_"):
        envvar = f"IQBA_{envvar}"
    value = os.getenv(envvar, default)
    return value if value is None else str(value).strip()


def is_env(envvar: str, value: str) -> bool:
    if (envvalue := get_env(envvar)) is None:
        return False
    return envvalue == value


def log_env_vars(logger: Logger) -> None:
    for var in _envvars:
        logger.info(f"Initializing with environment variable IQBA_{var}={get_env(var)}")
