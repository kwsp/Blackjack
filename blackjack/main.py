import sys
from game import Game


def main():
    print("Welcome to Blackjack!\n")
    g = Game()
    try:
        while True:
            g.play()
            g.print_score()

            inp = input("\nNew game? [(y)/n] ").strip().lower()
            if inp == "n":
                break

    except KeyboardInterrupt:
        g.print_score()


if __name__ == "__main__":
    main()

