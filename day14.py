# class property
# cs problem solving
# AND SOLUTION

# bro this guy's spelling is so bad
# what
'''
# oop/property.py
class Person:
    def __init__(self, age):
        self.age = age  # anyone can modify this freely

class PersonWithAccessors:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')

class PersonPythonic:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')

person = PersonPythonic(39)
print(person.age)  # 39 accessed as data attribute
person.age = 42    # accessed as data attribute
print(person.age)  # 42
person.age = 199   # ValueError: Age must be within [18, 99]

######################################################################

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

p = Person('Pedro')
print(p._name)

######################################################################

# Kilometer with property class
class Kilometer:
    def __init__(self, speed=0):
        self.speed = speed

    def to_mph(self):
        return (self.speed * 0.621371)

    # getter
    def get_speed(self):
        print('Getting value...')
        return self._speed

    # setter
    def set_speed(self, value):
        print('Setting value...')
        if value > 4520:
            raise ValueError('speed above 4520 has never been achieved')
        self._speed = value

    # creating a property object
    speed = property(get_speed, set_speed)

sedan = Kilometer(88)

print(sedan.speed)

print(sedan.to_mph())

sedan.speed = 700
print(sedan.__dict__['_speed'])

######################################################################

# Using @property decorator
class Kiolometer:
    def __init__(self, speed=0):
        self.speed = speed

    def to_mph(self):
        return round((self.speed * 0.621371))

    @property
    def speed(self):
        print('Getting value...')
        return self._speed

    @speed.setter
    def speed(self, value):
        print('Setting value...')
        if value > 4520:
            raise ValueError('speed above 4520 has never been achieved')
        self._speed = value


# create an object
sedan = Kiolometer(88)

print(sedan.speed)

print(sedan.to_mph())
print('Converted speed is ', sedan.speed)
print(sedan.__dict__)
# x15 = Kiolometer(4521)

######################################################################

# iterators/iterator.py
class OddEven:
    def __init__(self, data):
        self._data = data
        self.indexes = (list(range(0, len(data), 2)) + # concatenates
            list(range(1, len(data), 2)))
        return print(self.indexes)

    def __iter__(self): # returns stream of data of iterator
        return self

    def __next__(self): # returns the next item of the data stream
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration # prevents iteration going forever

oddeven = OddEven('ThIsIsCoOl!')
print(''.join(c for c in oddeven))
oddeven = OddEven('Hello')  # or manually...
it = iter(oddeven)  # this calls oddeven.__iter__ internally
print(next(it))  # H
print(next(it))  # l
print(next(it))  # o
print(next(it))  # e
print(next(it))  # l
'''

# why do you need to hide parts of the class anyway
# maybe it's just that i never needed that kind of stuff
# encapsulation doesn't really matter when you're not writing a library right?
# statically typed python frfr
# i guess the issue is that all the type inference has to be recalculated every time the code is run

# properties....
# because no private variables
# they let you customize get, set, and delete
# o.x
# o.x = 5
# del o.x
# or just not allow such a thing you know

# there are 2 ways (at least) to create a property

# decorator
class Person1:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        '''
        it also takes the getter docstring
        '''
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        raise RuntimeError('hey! don\'t delete Person.age! >:(')

# property()
class Person2:
    def __init__(self, age):
        self._age = age

    def getage(self):
        return self._age

    def setage(self, age):
        self._age = age

    def delage(self):
        raise RuntimeError('hey! don\'t delete Person.age! >:(')

    age = property(fget = getage, fset = setage, fdel = delage, doc = '''
        or one provided in property()
    ''')

# you don't need to provide all three functions
# the plain decorator makes a readonly attribute
class Person1:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

# iterables
# using __iter__ and __next__

# this is not my code
# somebody ought to be fired
class OddEven1:
    def __init__(self, data):
        self._data = data
        self.indexes = (list(range(0, len(data), 2)) + # concatenates
            list(range(1, len(data), 2)))
        return print(self.indexes)

    def __iter__(self): # returns stream of data of iterator
        return self

    def __next__(self): # returns the next item of the data stream
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration # prevents iteration going forever

class OddEven2:
    def __init__(self, data):
        self._data = data
        self.indexes = (
            i
            for it in [
                range(0, len(data), 2),
                range(1, len(data), 2)
            ]
            for i in it
        ) # so cool

    def __iter__(self):
        return self # already iterable <3

    def __next__(self):
        return self._data[next(self.indexes)] # automatically raises StopIteration

import itertools

class OddEven3:
    def __init__(self, data):
        self._data = data
        self.indexes = itertools.chain(
            range(0, len(data), 2),
            range(1, len(data), 2)
        ) # use the standard library :)

    def __iter__(self):
        return self # already iterable <3

    def __next__(self):
        return self._data[next(self.indexes)] # automatically raises StopIteration
