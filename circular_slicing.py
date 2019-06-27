"""
Circular Slicing.

Slicing from given index in circular way
"""
from itertools import cycle, islice

arr = [3, 2, 5, 4]
index = (int)(raw_input('Initial index: '))
steps = 0


print (arr)
for p in islice(cycle(arr), index, None):
    print p
    steps += 1
    if steps >= len(arr):
        break
