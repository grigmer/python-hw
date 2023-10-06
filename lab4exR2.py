def f(a, n, res = 1):
    while n != 0:
        if n > 0 :
            res *= a
            n -= 1
        else:
            res /= a
            n += 1
        f(a, n, res)
    return res


n = int(input())
p = int(input())


print(f(n, p))