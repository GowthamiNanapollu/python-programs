def function(camel):
    print("snakecase : ", end="")
    for i in camel:
        if i.isupper():
            print("_", end="")
            i = i.lower()
        print(i, end="")


def main():
    camelcase = input("enter the camel case : ")
    function(camelcase)


main()
