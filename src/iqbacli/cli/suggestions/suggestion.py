from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Suggestion:
    description: str
    command: str

    def to_dict(self: Suggestion) -> dict[str, Any]:
        return self.__dict__

    def to_rich_str(self: Suggestion, max_len: int) -> str:
        return f"[grey50]{f'({self.description})': <{max_len + 2}} {self.command}"
