from blackjack.game import Game
from blackjack.core import BasePlayer


def test_factory():
    g = Game()
    assert isinstance(g, Game)


def test_deal():
    g = Game()
    assert len(g.player.hand) == 0
    assert len(g.dealer.hand) == 0

    g.deal()
    assert len(g.player.hand) == 2
    assert len(g.dealer.hand) == 2
