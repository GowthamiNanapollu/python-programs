def deep1(user):
    user = user.lower()
    user = user.strip()
    if user == "42" or user == "forty-two" or user == "forty two" or user == "fortytwo":
        return True
    else:
        return False


def main():
    con = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    if deep1(con):
        print("Yes")
    else:
        print("No")


main()
