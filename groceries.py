def g_list():
    l = []
    d = {}
    while True:
        try:
            item = input("").strip().upper()
            l.append(item)
        except EOFError:
            break
    l.sort()

    for item in l:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1

    for item, count in d.items():
        print(f"{count} {item}")


g_list()
