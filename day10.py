# https://github.com/Gar-b-age/CookLikeHOC

class Person:
    species = 'human'

print(Person.species)
Person.alive = True
print(Person.alive)

man = Person()
print(man.species)
print(man.alive) # can access class attributes through any object
man.alive = 12
print(man.alive) # can also override them
del man.alive
print(man.alive) # delete member

man2 = Person()
Person.alive = False
print(man2.alive) # namespace lookup or smth idk - not copied at initialization

man.name = 'bobby timothy jonothon anders'
print(man.name)

# Gas stations, for example, might try to sell you a Reese’s Freeze, thanks to Sunny Sky’s unholy interventions. 
# https://getpocket.com/explore/item/the-truth-about-slushies-must-come-out?utm_source=firefox-newtab-en-us

class Square:
    side = 2
    def area(self):
        return self.side ** 2

s = Square()
print(s.area())
print(Square.area(s)) # you can also call it from the class (though i think this doesn't work with inheritance)

s.side = 12
print(s.area()) # it only depends on self.side <3
print(Square.area(s)) # (ignoring the source of the attribute)

# https://www.seriouseats.com/south-philly-style-roasted-long-hots-11813820

# "class variable are not good"
# specifically mutable class variables
# it's like mutable default arguments
# it's shared across all objects
# or all calls

# me when def __init__(self, ...):