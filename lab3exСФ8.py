with open('СФ8.txt', 'r') as f:
    n = int(f.readline())

    m = []
    max = None
    min = None
    indmax = 0
    indmin = 0
    for i in range(n):
        a = int(f.readline())
        m.append(a)
        if i == 0:
            min = a
            max = a
        else:
            if a > max:
                max = a
                indmax = i
            elif a < min:
                min = a
                indmin = i
    m[indmax] = min
    m[indmin] = max


with open('result.txt', 'w') as f:
    for i in m:
        f.write(str(i) + '\n')            