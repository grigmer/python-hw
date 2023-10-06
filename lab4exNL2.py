colors = set()


with open('NL2.txt', 'r') as f:

    all = f.readlines()

    for i in all:
        
        c = [int(j) for j in i.split()]
        
        if c[0] >= 230 and c[1] >= 230 and c[2] >= 230:
            colors.add(i)


print(len(colors))