from mmt.conversation import Conversation, Role, Utterance
from mmt.imitator import Imitator
from mmt.player import Player


PLAYER_RESPONSE = 'Hallo, Ich möchte ein espresso mit zwei zucker bitte.'


class DummyPlayer(Player):
    def respond(self, conversation: Conversation) -> Utterance:
        return Utterance(role=Role.PLAYER, text=PLAYER_RESPONSE)


class DummyImitator(Imitator):
    def respond(self, conversation: Conversation) -> Utterance:
        return Utterance(role=Role.IMITATOR, text='Hallo, was möchten sie?')

    def done(self, conversation: Conversation) -> bool:
        if len(conversation.utterances) == 0:
            return False
        last_utterance = conversation.utterances[-1]
        return last_utterance.role == Role.PLAYER and last_utterance.text == PLAYER_RESPONSE


def test_class_structure():
    player = DummyPlayer()
    barista_lady = DummyImitator()

    no_of_interaction = 0
    conversation = Conversation(utterances=[])
    while no_of_interaction < 5 and not barista_lady.done(conversation):
        barista_utterance = barista_lady.respond(conversation)
        conversation.utterances.append(barista_utterance)

        player_utterance = player.respond(conversation)
        conversation.utterances.append(player_utterance)

        no_of_interaction += 1

    assert no_of_interaction == 1
