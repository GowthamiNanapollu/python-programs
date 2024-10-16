def get_fraction():
    while True:
        f = input("Fraction :")
        f = f.strip()
        try:
            if "/" not in f:
                raise ValueError
            x, y = map(int, f.split("/"))
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                pass
            else:
                return x / y
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def get_percent(p):
    p = p * 100
    p = round(p)
    if p <= 1:
        print("E")
    elif p >= 99:
        print("F")
    else:
        print(f"{p}%")


def main():
    d = get_fraction()
    get_percent(d)


main()
