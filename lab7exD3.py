Drd = dict(zip(['A', 'U', 'G', 'C'], ['T', 'A', 'C', 'G'])) # Словарь из РНК в ДНК
Ddd = dict(zip(['A', 'T', 'G', 'C'], ['T', 'A', 'C', 'G'])) # Словарь из ДНК в ДНК
s1 = ''
s2 = ''
for i in input():
    s1 += Drd[i]
for i in s1:
    s2 += Ddd[i]
print(s1)
print(s2)