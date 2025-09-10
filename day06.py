# day06.py

def why(f):
    f(f)

#why(why) # do not

double = lambda x: x * 2
ns = [1, 2, 45, 7]
ns2 = [*map(double, ns)]
print(ns)
print(ns2)

print(bin.__doc__)

#help(bin)

# pycharm lets you format docstrings

xs = [2, 5, 8, 0, 0, 1, 0, None, '564', True, False, [], (), {}, set(), {6}, {4:5}, '', [2435, 8], (6, 7)]
print([*filter(None, xs)]) # None filter returns "truthy" items
print([*filter(lambda x: x, xs)]) # same as identity

# erm,.,,..., ackshually..,.,,,.
# if fun_test() returned 'ab', then
# p,q = fun_test() would not error

# you can specify the return type (and argument types) <3
# it doesn't check anything though

# your character has droped from 932 hit points to 43 hit points available

def x(x): yield 4

print(list(x(x)))