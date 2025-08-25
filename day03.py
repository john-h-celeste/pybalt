# me when zip()

print(list(zip(['a', 'b', 'c'], [1, 2, 3])))
print(list(zip('hello', range(1, 6))))

l = [1, 2, 3, 1]
l.append(1) # add value
l.count(1) # count value
l.extend([1, 4, 5, 7])
l.index(4)
l.insert(3, 6) # insert 6 at index 3
l.pop() # last element
l.pop(4) # element at index 4
l.remove(5) # remove value
# theres more but i was to slow

# set actually is mutable (with .add() and others)

# i didn't catch if he mentioned elif or not

s = 'Polytechnic'
print('%s...%s' % (s[0:3], s[len(s) - 3:len(s)]))

price = float(input('Enter a price:'))
dollars = int(price)
cents = int((price - dollars) * 100 + 0.5)
print(dollars, 'dollars', cents, 'cents')
print(f'{dollars} dollars {cents} cents')

names = ['Fritz']
names.insert(1, 'Ann')
names.insert(0, 'Melina')
names.pop(2)
names.append('Jorge')
print(sorted(names))

contacts = {'Jenny': 8765309, 'James': 5551212}
print(*contacts)
print('Jennys number is', contacts['Jenny'])
brian = contacts.get('James')
print('Brian has new number', brian)