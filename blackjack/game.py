import time
from core import Player, Dealer


# def print_cards(cards):
    # lines = ['  '] * 4
    # for v in cards:
        # lines[0] += "   ____ "
        # v = str(v)
        # if len(v) == 2:
            # lines[1] += "  |{}  |".format(v)
        # else:
            # lines[1] += "  |{}   |".format(v)
        # lines[2] += "  |    |"
        # lines[3] += "  |____|"

    # for l in lines:
        # print(l)

class Game():
    """Object that represents a game of Blackjack

    """
    WIN_1ST_RND = 2.5
    WIN = 2
    LOSS = 0
    TIE = 1
    SURRENDER = 0.5

    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.win_state = -1

        # Score counters
        self.score = {  
            "wins": 0,
            "ties": 0,
            "losses": 0,
            "surrenders": 0
        }

    def __repr__(self):
        return "Game( {}, {}, Score({}))".format(
            self.dealer,
            self.player,
            self.score_string()
        )

    def score_string(self):
        return "\nWins: {}, losses: {}, ties: {}, surrenders: {}\n".format(
            self.score["wins"],
            self.score["losses"], 
            self.score["ties"],
            self.score["surrenders"]
        )

    def print_score(self):
        """Method to print the current score
        """
        print(self.score_string())

    def update_score(self):
        if self.win_state >= self.WIN:
            self.score["wins"] += 1

        elif self.win_state == self.LOSS:
            self.score["losses"] += 1

        elif self.win_state == self.TIE:
            self.score["ties"] += 1

        elif self.win_state == self.SURRENDER:
            self.score["surrenders"] += 1

        else:
            raise ValueError("Invalid game win state")
        

    def clear_round(self):
        self.dealer.clear()
        self.player.clear()
        self.win_state = -1

    def deal(self):
        self.dealer.deal()
        self.player.deal()

    def dcard(self):
        return self.dealer.cards[0]
    
    def hit(self):
        self.player.hit()

    def check_current_round(self):
        """Check the result of the current round 
        against win conditions
        """
        if self.win_state != -1:
            if self.win_state == self.SURRENDER:
                print("You surrendered :)")
            elif self.win_state == self.WIN_1ST_RND:
                print("Perfect 21 from your first 2 cards! Win! 1.5x return!")

        elif self.player > 21:
            print("You busted :(")
            self.win_state = self.LOSS

        elif self.dealer > 21:
            print("Dealer busted, you win!")
            self.win_state = self.WIN

        elif self.dealer < self.player:
            print("You win!!!")
            self.win_state = self.WIN
            
        elif self.dealer > self.player.sum:
            print("You lost :(")
            self.win_state = self.LOSS

        elif self.dealer == self.player:
            print("Its a tie!")
            self.win_state = self.TIE

        else:
            raise ValueError("None of the game ending logic resolved")

    def play(self):
        self.clear_round()
        self.deal()
        print("Dealer's cards: {}, *".format(self.dcard()))
        self.dealer.print_cards(print_one=True)

        # Game loop
        while (self.player <= 21).any():
            print(self.player)
            self.player.print_cards()
            if len(self.player.cards) == 2:
                """First 2 cards dealt - check for 21 - able to surrender if cards are bad
                """
                if 21 in self.player.sum:
                    self.win_state = self.WIN_1ST_RND
                    break

                print("Hit [h],  pass [p] or surrender [s]? ", end="")
            else:
                print("Hit [h],  pass [p]? ", end="")

            inp = input().strip().lower()

            if inp == "h":
                self.hit()
                print("Got a card: {}".format(self.player.cards[-1]))
            elif inp == "p":
                break
            elif inp == "s":
                # implement surrender
                if len(self.player.cards) == 2:
                    self.win_state = self.SURRENDER
                    break
                else:
                    print("Can only surrender before you hit!")

        # If there are multiple sums, find the right one
        self.player.check_sum()
        print(self.player)

        # Dealer do his thing
        print("\nDealer reveal!")
        self.dealer.check_cards()
        print(self.dealer)
        self.dealer.print_cards()

        # Check win state of the current round
        self.check_current_round()

        # Update score counter
        self.update_score()


