with open('файлСФ1.txt', 'r') as f:
    n = int(f.readline())

    m = None
    for i in range(n):
        a = int(f.readline())
        if i == 0:
            m = a
        else:
            if a > m:
                m = a

with open('result.txt', 'w') as f:
    count = 0
    while m % 10 == 0:
        count += 1
        m //= 10

    f.write(str(count) + '\n')