def function(user):
    user = user.strip()
    user = user.lower()
    if "hello" in user:
        return "$0"
    elif user[0] == "h" and user != "hello":
        return "$20"
    else:
        return "$100"


def main():
    greet = input("greet the customer")
    print(function(greet))


main()
