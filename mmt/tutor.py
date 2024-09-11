from .actor import Actor
from .conversation import Conversation

class Tutor(Actor):
    def assist(conversation: Conversation):
        """assist the player when they get stuck."""
        pass

    def refine(conversation: Conversation):
        """refine players response."""
        pass

    def respond_ideally(conversation: Conversation):
        """ideal player response given the conversation."""
        pass