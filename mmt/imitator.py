from .actor import Actor
from .conversation import Conversation


class Imitator(Actor):
    def done(conversation: Conversation) -> bool:
        """if the objective is acheived."""
        pass
