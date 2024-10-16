import sys


def get_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        return sys.argv[1]


def count_lines(file="line.py"):
    count = 0
    if file[-3:] != ".py":
        sys.exit("Not a python file")
    else:
        try:
            with open(file, "r") as lfile:
                lines = lfile.readlines()
                for line in lines:
                    line = line.lstrip()
                    if not line.startswith("#") and not line == "":
                        count += 1

        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            return count


def main():
    file_name = get_file()
    lines = count_lines(file_name)
    print(lines)


if __name__ == "__main__":
    main()
