from core import Player, Dealer


class Game():
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.win = None

    def __repr__(self):
        return "Game( {}, {} )".format(
            self.dealer,
            self.player
        )

    def clear(self):
        self.dealer.clear()
        self.player.clear()
        self.win = None

    def deal(self):
        self.dealer.deal()
        self.player.deal()

    def dcard(self):
        return self.dealer.cards[0]
    
    def pcard(self):
        return self.player.cards

    def psum(self):
        return self.player.sum
    
    def player_check(self):
        self.player.check_sum()

    def hit(self):
        self.player.hit()

    def play(self):
        self.deal()
        print("Dealer's cards: {}, *".format(self.dcard()))

        # Game loop
        while (self.player <= 21).any():
            print(self.player)
            inp = input("Hit [h] or pass [p]? ")
            if inp.lower() == "h":
                self.hit()
                print("Got a card: {}".format(self.player.cards[-1]))
            elif inp.lower() == "p":
                break

        # If there are multiple sums, find the right one
        self.player_check()
        print(self.player)

        # Game result
        if not self.player <= 21:
            print("You busted :(")
            self.win = False

        else:
            # print("\nDealer currently has: {}, sum: {}".format(
                    # self.dealer.cards, self.dealer.sum
                # ))
            self.dealer.check_cards()
            print(self.dealer)

            if self.dealer > 21:
                print("Dealer busted, you win!")
                self.win = True

            elif self.dealer > self.player.sum:
                print("You lost :(")
                self.win = False

            elif self.dealer == self.player:
                print("Its a tie!")
                self.win = None

            elif self.dealer < self.player:
                print("You win!!!")
                self.win = True

            else:
                print("I don't know what's happening")
                breakpoint()


