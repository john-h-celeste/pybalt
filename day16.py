# exceptions and context manager

#raise ValueError('nope')

# syntax
try:
    pass
except Exception as e:
    pass # captured error
except Exception:
    pass # error
except (TypeError, ZeroDivisionError) as e:
    pass # multiple exception types
except:
    pass # any error
else:
    pass # no errors
finally:
    pass # anyway (before raising or reraising or return)

# you can use try + finally to close a file....
# or you can use with.....

import sys
print('bingus', file = sys.stderr)

# w vs x file modes
# w deletes the existing file
# x errors if there is an existing file

# rt / rb
# default text i think
# rb reads b'' strings

# pathlib
import pathlib

p = pathlib.Path('day17.py')
print(p.is_file())
print(p.parent.absolute())
print(p.parent.is_dir())

# io.StringIO / io.BytesIO
import io

with io.StringIO() as f:
    f.write('wewewewe')
    print(f.getvalue())

# json and csv

# data = [*csv.reader(f)]
# csv.writer(f).writerows(data)

# serialization and deserialization
# i should make a class or something for serialization

# pickle
# dataclass
import pickle
import dataclasses
@dataclasses.dataclass
class X:
    a: int
    b: str
    def p(self):
        print(f'X({self.a}, {self.b})')

# pickle.dump(o, f)
# pickle.load(f)

import numpy
import random
import functools
import operator

class NodeGroup:
    def __init__(self, size):
        self.parent = None
        self.size = size
        self.children = []
    
    def choose(self, node):
        self.chosen = node
        for ws,c in self.children:
            choice = random.choices([*range(c.size)], weights = ws[node, :])[0]
            c.choose(choice)
    
    def addchild(self, child):
        assert child.parent == None
        child.parent = self
        ws = numpy.random.random_sample((self.size, child.size))
        ws /= ws.sum(1, keepdims = True)
        self.children.append((ws, child))
    
    def calcupward(self):
        self.vs = []
        for ws,c in self.children:
            c.calcupward()
            self.vs.append((ws * c.u).sum(0))
        self.u = functools.reduce(operator.mul, self.vs)

g1 = NodeGroup(2)
g2 = NodeGroup(3)
g1.addchild(g2)
print(g1.children[0])

g2.u = numpy.array([0, 0, 1])
g1.calcupward()
print(g1.u)