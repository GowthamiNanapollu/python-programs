import requests
import sys
import json


def get_coins():
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        if len(sys.argv) == 2:
            coins = float(sys.argv[1])
            return coins
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)


def get_cost():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        cost = data["bpi"]["USD"]["rate_float"]
        return cost

    except requests.RequestException:
        sys.exit()


def find_cost(no, price):
    total = no * price
    print(f"${total:,.4f}")


def main():
    no = get_coins()
    pr = get_cost()
    find_cost(no, pr)


if __name__=="__main__":
    main()
