from .deck import Hand


class Player(object):
    def __init__(self, name, hand=None):
        self.name = name
        self.hand = hand or Hand()

    def discard(self, idx):
        return self.hand.pop(idx)
