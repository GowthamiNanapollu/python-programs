def machine():
    amountdue = 50
    amount = 0
    while True:
        print("Amount Due:", amountdue)
        icoin = input("insert a coin : ")
        icoin = int(icoin)
        if icoin == 25 or icoin == 10 or icoin == 5:
            amountdue = amountdue - icoin
            amount = amount + icoin
            if amount >= 50:
                if amount == 50:
                    changeowned = 0
                    print("Change Owed:", 0)
                    break
                else:
                    changeowned = amount - 50
                    print("Change Owed:", changeowned)
                    break

        else:
            continue


machine()
