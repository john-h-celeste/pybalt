# nested functions
# heart menosnji

v = 0
def outer():
    v = 1
    def inner():
        v = 2
        print(v)
    inner()
    print(v)
outer()
print(v)

# local enclosing global builtins
# namespace in __dict__

# bro how do you spell it immuatable
# like it's one letter but
# do you even spellcheck
# also set is mutable
# just thought you should know

# four types of argument
# positional keyword iterable (list) dictionary

def f(a, b):
    print(a, b)

f(1, 1)
f(b = 1, a = 2)
f(*[3, 8])
f(**{'a': 4, 'b': 34})

# default parameters are mutable >:(

# when you can configure the default operators and functions :)