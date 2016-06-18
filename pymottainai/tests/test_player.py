from pymottainai.engine.player import Player


def test_player_hand_size():
    player = Player(name="foo",
                    hand=[1, 2, 3, 4, 5, 6])
    assert player.over_limit

    player.discard(4)
    assert not player.over_limit


def test_player_add_card():
    player = Player(name="foo",
                    hand=[1, 2, 3, 4])
    player.add_card(5)

    assert 5 in player.hand
