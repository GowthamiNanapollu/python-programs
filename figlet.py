import sys
import random
from pyfiglet import Figlet


def zeroarg():
    li = [
        "3-d",
        "3x5",
        "5lineoblique",
        "acrobatic",
        "alligator",
        "alligator2",
        "alphabet",
        "avatar",
        "banner",
        "banner3-D",
        "banner3",
        "banner4",
        "barbwire",
        "basic",
        "bell",
        "big",
        "bigchief",
        "binary",
        "block",
        "bubble",
        "bulbhead",
        "caligraphy",
        "catwalk",
        "chunky",
        "coinstak",
        "colossal",
        "computer",
        "contessa",
        "contrast",
        "cosmic",
    ]
    figlet = Figlet()
    s = input("Input:")
    f = random.choice(li)
    figlet.setFont(font=f)
    print(figlet.renderText(s))


def twoarg(f):
    figlet = Figlet()
    s = input("Input:")
    figlet.setFont(font=f)
    print(figlet.renderText(s))


def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet = Figlet()
            li = figlet.getFonts()
            if sys.argv[2] in li:
                font = sys.argv[2]
                twoarg(font)
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    elif len(sys.argv) == 1:
        zeroarg()
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
