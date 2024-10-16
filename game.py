import random
import sys


def main():
    level = get_input()
    game(level)


def get_input():
    ch = True
    while ch:
        try:
            level = int(input("Level:"))
            if level > 0:
                ch = False
                return level
            if level <= 0:
                raise ValueError
        except ValueError:
            pass


def game(level):
    ran = random.randint(1, level)
    ch = True
    while ch:
        try:
            guess = int(input("Guess:"))
            if guess <= 0:
                raise ValueError
        except ValueError:
            pass
        else:
            if guess < ran:
                print("Too small!")
                ch = False
            elif guess > ran:
                print("Too large!")
                ch = True
            else:
                print("Just right!")
                sys.exit(1)


main()
