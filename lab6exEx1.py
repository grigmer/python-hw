def flexible_get(a, b):
    c = int(b)
    try:
        return a[c]
    except IndexError:
        return None
print(flexible_get([i for i in input()], float(input())))