import numpy as np


class Cards:
    available_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    JQK = ['J', 'Q', 'K']

    @staticmethod
    def new_card():
        return Cards.available_cards[np.random.randint(13)]


class BasePlayer(Cards):
    def __init__(self):
        self.cards = []
        self.sum = np.zeros(1, dtype=np.uint8)

    def __repr__(self):
        return "{}: cards {}, sum {})".format(
                str(self.__class__).split(".")[-1].split("'")[0],
                self.cards,
                self.sum
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
            "cards": self.cards,
            "sum": self.sum,
        }

    def deal(self):
        """Get a new hand
        """
        self.cards = [self.new_card(), self.new_card()]
        self.calc_sum()

    def hit(self):
        """Get a new card
        """
        self.cards.append(self.new_card())
        self.calc_sum()

    def calc_sum(self):
        """Calculate the sum of the current hand
        """
        self.sum = np.zeros(1, dtype=np.uint8)

        for val in self.cards:

            # Handle non-numeric values
            if isinstance(val, str):
                if val in self.JQK:
                    self.sum += 10
                elif val == "A":
                    self.sum += 1
                    self.sum = np.append(self.sum, self.sum + 10)
                else:
                    raise ValueError("Card not recognised.")

            # Numeric values
            elif isinstance(val, int):
                self.sum += val
            else:
                raise TypeError("Unrecognised type in cards array.")
        
    def clear(self):
        """Clear the hand
        """
        self.cards = []
        self.sum = np.zeros(1, dtype=np.uint8)


class Player(BasePlayer):
    def __init__(self):
        BasePlayer.__init__(self)

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
        BasePlayer.__init__(self)

    def check_cards(self):
        """Check if the dealer needs to draw new cards
        """
        while (self.sum <= 21).any():

            if 21 in self.sum:
                """Check for 21
                """
                self.sum = 21
                break

            if np.bitwise_and(
                    (self.sum <= 21),
                    (self.sum > 16)
                ).any():
                """
                If the dealer sum is larger than 16 and
                smaller or equals to 21, store that sum
                """
                self.sum = self.sum[self.sum > 16][0]
                break
            else:
                """
                Dealer sum <= 16, hit again
                """
                self.hit()
            

