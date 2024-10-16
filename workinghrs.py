import re

def main():
    print(convert(input("Hours: ").strip()))


def convert(s):

        pattern = r"^([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([0-9]|1[0-2]):?([0-5][0-9])? (PM|AM)$"
        matches = re.search(pattern, s)

        if matches:
            if matches.group(3) =="AM":
                hour1 = int(matches.group(1))
                if hour1 == 12:
                     hour1 = 0
            else:
                 hour1 = int(matches.group(1))+12

            if matches.group(6) == "AM":
                 hour2 = int(matches.group(4))
            else:
                  hour2 = int(matches.group(4)) + 12
                  if hour2 == 24:
                     hour2 = 12


            min1 = int(matches.group(2)) if matches.group(2) else 0
            min2 = int(matches.group(5)) if matches.group(5) else 0
            return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"
        else:
            raise ValueError



if __name__ == "__main__":
    main()
