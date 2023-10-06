cards = set()


with open('NL1.txt', 'r') as f:

    all = f.readlines()

    for i in all:
        
        c = [j for j in i.split(", ")]
        c[-1] = (c[-1])[:-1]
        
        for k in c:
            cards.add(k)


if len(cards) == 8:
    print("ДА")
else:
    print("НЕТ")