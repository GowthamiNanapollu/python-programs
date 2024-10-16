def get_input(c):
    while c:
        try:
            date = input("Date:")
            date = date.strip()
            if date[0].isalpha() and date[1].isalpha():
                c=test_alpha(date)
            if date[0].isdigit():
                c=test_numeric(date)
        except ValueError:
            pass


def test_alpha(date):
    if "/" in date:
        return True
    if ","not in date or " " not in date:
        return True
    date = date.replace(" ", "/")
    date = date.replace(",", "")
    mon = {
        "January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31,
        "September": 30, "October": 31, "November": 30, "December": 31
    }
    mon1 = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }
    try:
        mm, dd, yy = date.split("/")
        dd = int(dd)
    except ValueError:
        return True
    else:
        mm=mm.title()
        if mm not in mon:
            return True
        elif dd > mon[str(mm)]:
            return True
        else:
            print(f"{yy}-{mon1[mm]:02}-{dd:02}")
            return False



def test_numeric(date):
    mon = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30,
           '12': 31}
    date = date.strip()
    try:
        mm, dd, yy = date.split("/")
        mm = int(mm)
        dd = int(dd)
        if mm > 12 or dd > mon[str(mm)]:
            return True
        else:
            print(f"{yy}-{mm:02}-{dd:02}")
            return False
    except ValueError:
        return True

def main():
     ch=True
     get_input(ch)
main()
