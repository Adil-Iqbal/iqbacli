from __future__ import annotations

import dataclasses
from enum import Enum
from typing import TypedDict


class MessageType(Enum):
    SUCCESS = "success"
    INFO = "info"
    WARN = "warn"
    ERROR = "error"


class MessageDict(TypedDict):
    message: str
    type: str


@dataclasses.dataclass
class Message:
    message: str
    type: MessageType

    def to_dict(self: Message) -> MessageDict:
        return {"message": self.message, "type": self.type.value}
