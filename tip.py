def dollars_to_float(d="$50"):
    d=d.replace("$","")
    d=float(d)
    return d
def percent_to_float(p="15%"):
    p=p.replace("%","")
    p=float(p)
    p=p/100
    return p
def main():
    dollars =dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
main()
