def main():
 time=input("enter the time ")
 hour=convert(time)
 print(func(hour))


def convert(time):
    time=time.strip()
    hours,min=time.split(":")
    min=min.strip()
    if len(min) == 2:
        min = float(min) / 60
    else :
      min=float(min)/6
    hours=float(hours)
    hours=hours+min
    return hours
def func(hour):
    if 7<= hour <=8:
        return "breakfast time"
    elif 12<= hour <=13:
        return "lunch time"
    elif 18<= hour <=19:
        return "dinner time"
    else :
        return ""




if __name__ == "__main__":
    main()
