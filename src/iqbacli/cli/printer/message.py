from __future__ import annotations

import copy
import dataclasses
from enum import Enum
from typing import Any


class MessageType(Enum):
    SUCCESS = "success"
    INFO = "info"
    WARN = "warn"
    ERROR = "error"


@dataclasses.dataclass
class Message:
    message: str
    type: MessageType

    def to_dict(self: Message) -> dict[str, Any]:
        message_dict = copy.deepcopy(self.__dict__)
        message_dict["type"] = self.type.value
        return message_dict
