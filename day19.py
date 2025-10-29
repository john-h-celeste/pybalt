# debugging <3

# you can use print statements
# but it's hard to clean out

# but you can also use pdb.set_trace()
# and breakpoint()

#import pdb
#pdb.set_trace()

# python -m pdb py.py

#breakpoint

# s[tep] - steps into
# n[ext] - next line in this function
# un[til] [line] - execute until line greater than current or given line
# r[eturn] - until the current function returns
# c[ont[inue]] - until next breakpoint
# j[ump] [line] - only in bottom frame

# pycharm can do debugging too
# breakpoints
# step into
# watch variables

# logging module
# i never use this
# maybe i should start
# this would be useful for the 
import logging

logger = logging.getLogger('bingus log')

logging.basicConfig(
    filename = 'day129log.txt',
    level = logging.INFO,
    format = '[%(asctime)s] %(levelname)s: %(message)s',
    datefmt = '%m/%d/%Y %I:%M:%S %p',
)

logger.info('hi guys it\'s me bingus')

# profiling

# python -m cProfile py.py
# also timeit
# pycharm has builtin profiling too