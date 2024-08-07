import sys
from game import Game

def print_score(sc):
    print("\nWins: {}, losses: {}, ties: {}\n".format(
        sc["wins"], sc["losses"], sc["ties"]
    ))


def main():
    print("Welcome to Blackjack!\n")
    g = Game()
    score = {
        "wins": 0,
        "ties": 0,
        "losses": 0
    }
    try:
        while True:
            g.play()

            if g.win is None:
                score["ties"] += 1
            elif g.win:
                score["wins"] += 1
            else:
                score["losses"] += 1

            inp = input("\nNew game? [(y)/n] Show score? [s] ").strip().lower()

            if inp == "n":
                print_score(score)
                break
            elif inp == "s":
                print_score(score)

    except KeyboardInterrupt:
        print_score(score)
        sys.exit("Bye bye!")


if __name__ == "__main__":
    main()

