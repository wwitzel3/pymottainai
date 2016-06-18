import random

from .env import ALL_CARDS


class Deck(object):
    def __init__(self):
        self.cards = ALL_CARDS[:]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def return_card(self, card):
        self.cards.insert(0, card)


class Hand(object):
    def __init__(self, cards=None):
        self.cards = cards or list()

    def pop(self, idx):
        return self.cards.pop(idx)

    def __len__(self):
        return len(self.cards)
