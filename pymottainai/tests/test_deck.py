from pymottainai.engine.deck import Deck


def test_return_card():
    deck = Deck()

    card = deck.draw()
    assert deck.cards[0] != card

    deck.return_card(card)
    assert deck.cards[0] == card
