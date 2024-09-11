from dataclasses import dataclass
from enum import Enum


class Role(Enum):
    PLAYER = 0
    IMITATOR = 1
    TUTOR = 2


@dataclass
class Utterance:
    """Class to store an individual utterance."""
    role: Role
    text: str


@dataclass
class Conversation:
    """Class to store conversations."""
    utterances: list[Utterance]
