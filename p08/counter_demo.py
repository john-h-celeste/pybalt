import counter

tally = counter.Counter()

tally.click()
tally.click()

result = tally.getValue()
print('Result is', result)

tally = counter.CounterMax(2)

tally.click()
tally.click()
tally.click()
tally.click()

result = tally.getValue()
print('Result is', result)

tally = counter.CounterStr()

tally.click()
tally.click()

result = tally.getValue()
print('Result is', result)