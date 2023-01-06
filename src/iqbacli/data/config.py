from __future__ import annotations

import json
import dataclasses
from pathlib import Path


@dataclasses.dataclass
class Config:
    ...

    @staticmethod
    def get_config(config_path: Path) -> Config:
        with open(str(config_path.absolute()), "r") as config_file:
            return Config(**json.load(config_file))
