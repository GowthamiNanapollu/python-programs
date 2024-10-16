def cost():
    total=0.00
    d={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    item=[]
    while True:
        try:
            item=input("Item:").strip()
            item=item.title()
            if item not in d:
                pass
            else:
                total=total+d[item]
                print(f"${total:.2f}")

        except EOFError:
            break


cost()


