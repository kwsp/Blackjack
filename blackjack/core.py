import numpy as np


deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
JQK = ["J", "Q", "K"]
deck_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def _new_card():
    return deck[np.random.randint(13)]


def _print_cards(hand, print_one=False, pad_spaces=4):
    lines = ["  "] * pad_spaces
    if print_one:
        hand = hand[:1]

    for v in hand:
        lines[0] += "   ____ "
        v = str(v)
        if len(v) == 2:
            lines[1] += "  |{}  |".format(v)
        else:
            lines[1] += "  |{}   |".format(v)
        lines[2] += "  |    |"
        lines[3] += "  |____|"

    for l in lines:
        print(l)


class BasePlayer:
    def __init__(self):
        self.hand = []
        self.sum = np.zeros(1, dtype=np.uint8)
        self.pad_spaces = 4

    def __repr__(self):
        return "{}: hand {}, sum {})".format(
            str(self.__class__).split(".")[-1].split("'")[0], self.hand, self.sum
        )

    def __eq__(self, value):
        return self.sum == value

    def __gt__(self, value):
        return self.sum > value

    def __ge__(self, value):
        return self.sum >= value

    def __lt__(self, value):
        return self.sum < value

    def __le__(self, value):
        return self.sum <= value

    def __call__(self):
        return {
            "hand": self.hand,
            "sum": self.sum,
        }

    def deal(self):
        """Get a new hand"""
        self.hand = [_new_card(), _new_card()]
        self.calc_sum()

    def hit(self):
        """Get a new card"""
        self.hand.append(_new_card())
        self.calc_sum()

    def calc_sum(self):
        """Calculate the sum of the current hand"""
        self.sum = np.zeros(1, dtype=np.uint8)

        for val in self.hand:

            # Handle non-numeric values
            if isinstance(val, str):
                if val in JQK:
                    self.sum += 10
                elif val == "A":
                    self.sum += 1
                    self.sum = np.append(self.sum, self.sum + 10)
                else:
                    breakpoint()
                    raise ValueError("Card not recognised.")

            # Numeric values
            elif isinstance(val, int):
                self.sum += val
            else:
                breakpoint()
                raise TypeError("Unrecognised type in hand array.")

    def print_cards(self, print_one=False):
        _print_cards(self.hand)

    def clear(self):
        """Clear the hand"""
        self.hand = []
        self.sum = np.zeros(1, dtype=np.uint8)


class Player(BasePlayer):
    def __init__(self):
        super().__init__()

    def check_sum(self):
        idx = self.sum <= 21
        if (idx).any():
            self.sum = self.sum[idx][-1]
        else:
            self.sum = self.sum.min()


class Dealer(BasePlayer):
    """Dealer Object

    fix [6, 3, 2, 'A']
    """

    def __init__(self):
        super().__init__()
        self.pad_spaces = 6

    def check_cards(self):
        """Check if the dealer needs to draw new hand"""
        while True:

            if 21 in self.sum:
                """Check for 21"""
                self.sum = 21
                break

            elif np.bitwise_and((self.sum <= 21), (self.sum > 16)).any():
                """
                If the dealer sum is 17 or more and
                not larger than 21, store that sum
                """
                self.sum = self.sum[self.sum > 16][0]
                break

            elif (self.sum <= 16).any():
                """
                Dealer sum <= 16, hit again
                """
                self.hit()
                if not (self.sum <= 21).any():
                    self.sum = self.sum[0]
                    break

    def print_cards(self):
        _print_cards(self.hand, print_one=True, pad_spaces=4)
