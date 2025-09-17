# unpacking_operator.py
a_tuple = (1,2,3,4,5,6,7)
a_list = [22,33,44,55]
def some_dict():
  a_dict = {'abe': 123, 'doe': 345, 'ken': 789}
  return a_dict

print(*a_tuple)
print(*a_list)
print(*some_dict())

hp_damage = lambda hp, dmg: hp - dmg
damage = 20
hp = 100
print(f'Your character took {damage} points of damge')
print(f'Your character has droped from {hp} hit points to \ {hp_damage(hp,damage)} hit points available')

def scoreToNumber(score):
  score = str.upper(score)
  result = 0
  first = score[0]
  if first == "G" :
    result = 10
  elif first == "O" :
    result = 5
  elif first == "P" :
    result = 3
  return result

def main():
  score1 = input('Enter score 1 as Great, Ok or Poor: ')
  score2 = input('Enter score 2 as Great, Ok or Poor: ')
  score3 = input('Enter score 3 as Great, Ok or Poor: ')
  x1 = scoreToNumber(score1)
  x2 = scoreToNumber(score2)
  x3 = scoreToNumber(score3)
  xmax = max(x1, x2, x3)
  some_avg = (x1 + x2 + x3) / 3
  print(f'The maximum score was {xmax}')
  print(f'The avg score on 1-10 scale would have been {round(some_avg, 2)}')

# nah
#main()



# strip off dashes
def strip_string(b_function):
    def wrapper():
        func = b_function()
        strip_string = func.strip('-')
        return strip_string
    return wrapper

#create upper case version of clli code
def uppercase_decorator(some_function):
  def a_wrapper():
    func = some_function()
    make_uppercase = func.upper()
    return make_uppercase

  return a_wrapper

@strip_string
@uppercase_decorator
def clli_code():
  print('The Florida router clli code is', end = '')
  return '---tpaflxacg19----'

print(clli_code())
# Double click to copy code

# map.grades.py
# produce list of tuples
grades = [95, 88, 85, 75]
letter_grade = ['A', 'B+', 'B', 'C']
print('The original list ',letter_grade)
print('The zipped tuples ', list(zip(letter_grade, grades)))
print('Next is a map-lambda version')
print(list(map(lambda *a: (a[0], a[1]), letter_grade, grades)))  # equivalent to zip


# filter_clli.py
# returns only clli codes located in Florida or California
clli_names = ['flxa99443oc', 'gaxb32443oc', 'caxo99323oc', 'flxa11443ds']
print(list(filter(lambda x: x[0].upper() in 'FC', clli_names)))

# list_comp1.py
print([(x, y) for x in ['a', 'b', 'c'] for y in ['first','b', 3] if x != y])

# conv_neg_pos_nocomp.py
a_list = [7, 5, -4, 6]
print([-x for x in filter(lambda x: x < 0, a_list)])

# listcomp_vs_genexp.py
# list comprehension vs generator expression
import sys
a = [x for x in range(1000000)] #list comp
b = (x for x in range(1000000))
print('list comp byte size is ',sys.getsizeof(a))
print('generator expression byte size is ',sys.getsizeof(b))
# double click to copy
