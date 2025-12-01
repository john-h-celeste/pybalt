s = open('input1').read()
lines = s.strip().split()
d = {'L': -1, 'R': 1}
import itertools
print('part 1', [a % 100 for a in itertools.accumulate([d[l[0]] * int(l[1:]) for l in lines], initial = 50)].count(0))
print('part 2', [a % 100 for a in itertools.accumulate(itertools.chain.from_iterable(itertools.repeat(d[l[0]], int(l[1:])) for l in lines), initial = 50)].count(0))
