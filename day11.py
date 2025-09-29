# overloading/overriding
# overloading is more difficult in python i think
# "not in python but we can mimic it"
# static and class methods

# overloading can be done with default arguments or unpacking

# overriding is the same in python as in c++
# though you can change the signature
# there's no restriction

import abc
import math

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class WeirdSquare(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.radius * self.radius

#s = Shape()
#s.area()
#s.perimeter()
s = Circle(5)
s.area()
s.perimeter()
#s = WeirdSquare(5)
#s.area()
#s.perimeter()

# super().__init__() to initialize parent class
# note: method (and class member) resolution order
# super() goes one class up the method resolution order
# mro is breadth first

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)

# static methods are not passed the implicit self argument
# and can be used without an instance
# should be used for utility functions

@staticmethod # these don't have to be defined inside a class
@staticmethod
@staticmethod # it can also be nested (i'm such a prankster)
def a():
    pass

a()

print(a)

# class methods are not directly callable
# they have to be called through a class
# takes the class as the first parameter
# can be used to make utility functions
# that take into account the class they were called from

class X:
    x = 1
    _x = 2
    __x = 3

X.__x = 4
print(X.__dict__)
print(X().__dict__)