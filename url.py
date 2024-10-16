import re


def main():
    print(parse(input("HTML :")))


def parse(str):

    pattern = r'src="https?://(?:www.)?youtube.com/embed(/[a-z0-9A-Z]+)"'
    matches = re.search(pattern, str)
    if matches:
        return "https://youtu.be" + matches.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
