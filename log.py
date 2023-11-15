from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Literal


@dataclass
class Message:
    role: Literal["user", "assistant", "system"]
    content: str

    def __str__(self) -> str:
        return f"{self.role}: {self.content}"


class Log:
    def __init__(self):
        self.messages: list[Message] = []

    def set_system_message(self, content: str) -> None:
        if self.messages and self.messages[0].role == "system":
            self.messages[0] = Message(role="system", content=content)
        else:
            self.messages.insert(0, Message(role="system", content=content))

    def save(self, path: Path) -> None:
        if not os.path.exists(path.parent):
            os.makedirs(path.parent)
        with open(path, "w") as f:
            json.dump(self.messages, f, indent=4)

    def load(self, path: Path) -> None:
        with open(path, "r") as f:
            self.messages = json.load(f)
