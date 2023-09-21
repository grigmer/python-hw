def f(a='a', b="b", c="c", d="b", e="a"):
    print(a, d, b, c, e)
f('a', 'b')
f('b', 'a')
f('a', 'b', 'f')
f('a', 'b', d='d')
f('*', '*', '*', '*', '*')