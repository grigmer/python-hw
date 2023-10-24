with open('dict.txt', 'r') as f:
    d = dict()
    for line in f:
        key, val = line.split(" -> ")
        if val[-1] == '\n':
            d[val[:-1]] = key
        else:
            d[val] = key

with open('result.txt', 'w') as f:
    for key in d:
        f.write(key + ' -> ' + d[key] + '\n')