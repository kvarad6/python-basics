
# reference: https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

# reduce(fun, seq) -> apply a particular function passed in its argument to all of the list elements
# reduce() function is defined in "functools" modules.

# Sum of all elements in a list using lambda and reduce() function

from functools import reduce

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x,y: x+y), li)

print("sum: ", sum)

#------------------------------------

# Find the maximum element in a list using lambda and reduce() function

li = [5, 8, 10, 20, 50, 100]

maxElement = reduce((lambda a,b: a if a>b else b), li)
print("maxElement: ", maxElement)

#------------------------------------

# Reduce vs Accumulate

# differences:
# reduce -> functools module | accumulate -> itertools module
# reduce(fun, seq) | accumulate(seq, fun)

lis = [1, 3, 4, 10, 4]

import functools
print(functools.reduce(lambda x,y: x+y, lis))

import itertools
print(list(itertools.accumulate(lis, lambda x,y: x+y)))

#--------------------------------------------------------





