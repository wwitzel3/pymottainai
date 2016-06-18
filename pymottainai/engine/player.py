from .deck import Hand
from .env import HAND_SIZE


class Player(object):
    def __init__(self, name, hand=None, task=None):
        self.name = name
        self.hand = hand or Hand()
        self.task = task

    def add_card(self, card):
        self.hand.append(card)

    def discard(self, idx):
        return self.hand.pop(idx)

    @property
    def over_limit(self):
        return len(self.hand) > HAND_SIZE
