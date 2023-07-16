# Short Question Description: What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# Author: @SelimGunal
# not Finished on 16.07.2023

import copy

theString = ["0","1","2","3","4","5","6","7","8","9"]
fixed = -1
remain = 10

numbers = []

result = 0

def permutation(theString, fixed, remain):
    fixed += 1
    remain -= 1
    cache = theString[fixed]


    if remain == 0:
        numbers.append(theString)
        return None

    for i in range(fixed, len(theString)):
        cacheString = copy.copy(theString)

        cacheString[fixed] = cacheString[i]
        cacheString[i] = cache
        permutation(cacheString, fixed, remain)



permutation(theString, fixed, remain)
