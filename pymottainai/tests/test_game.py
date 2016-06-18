import pytest

from pymottainai.engine.game import Game
from pymottainai.engine.player import Player
from pymottainai.engine.deck import Hand
from pymottainai.engine.card import Card


@pytest.mark.parametrize("player_count", [2, 3], ids=["2player", "3player"])
def test_game_setup(player_count):
    game = Game(player_count=player_count)

    assert len(game.players) == player_count


def test_game_deal():
    game = Game(player_count=3)

    hands = game.deal()
    assert len(hands) == 3

    single_hand = hands[0]
    assert len(single_hand) == 5


def test_player_discard():
    player = Player(name="foo", hand=Hand(cards=[Card(name="bar")]))
    card = player.discard(0)

    assert card.name == "bar"


def test_game_floor_setup():
    players = [Player(name="bar"), Player(name="baz"), Player(name="foo")]
    for player in players:
        player.hand = Hand(cards=[Card(name="{}-card".format(player.name),
                                       owner=player)])

    game = Game(players=players)

    for player in game.players:
        game.floor.append(player.discard(0))

    assert game.turn_count == 0
    assert game.current_player is None
    assert game.start_player == players[0]
