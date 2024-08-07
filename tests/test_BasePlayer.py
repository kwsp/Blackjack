from blackjack.core import BasePlayer


def test_factory():
    p = BasePlayer()
    assert isinstance(p, BasePlayer)


def test_deal():
    p = BasePlayer()
    p.deal()
    assert len(p.hand) == 2
    p.clear()
    assert len(p.hand) == 0


def test_hit():
    p = BasePlayer()
    l = len(p.hand)
    for i in range(5):
        p.hit()
        temp_l = len(p.hand)
        assert temp_l == l + 1
        l = temp_l


def test_calc_sum():
    p = BasePlayer()

    p.hand = [2, 4]
    p.calc_sum()
    assert p.sum[0] == 6

    p.hand = ["A", 10]
    p.calc_sum()
    assert 11 in p.sum
    assert 21 in p.sum


def test_operators():
    p = BasePlayer()
    p.hand = [3, 6]
    p.calc_sum()
    assert p.sum < 10
    assert p.sum > 8
