print(bool(100))
print(bool(-100))
print(bool(0))
print(bool(1))
print(bool(3))
print(not 3)

print(0.3 + 0.1) # ok.
print(0.3 - 0.1) # bruh

print(round(0.3 - 0.1, 2)) # real

print('{:.3f}'.format(9.9899))

import decimal

decimal.Decimal('0.143')

str3 = '''This is built with.
... so it can span multiple lines.''' ' b'

print('This string has both '"'"'single'"'"' and ' + chr(92) + '"''double' + chr(92) + chr(34) + chr(32) + 'qu'"otes")

print('\N{greek small letter pi}') # what
print('\U000003c0')
print(bytes('\U000003c0', 'utf-8'))

print('the trouble is that you think you have time'[2:14:3])

# two-pul
t = ()

a = (1,)

wea = (1, 3, 4)

a,b,c = 1, 3, 5 # this is a tuple yes

# least
# like an array <3
# add the elemnent with the comma

print([x + 5 for x in [1, 2, 5, 6]])

