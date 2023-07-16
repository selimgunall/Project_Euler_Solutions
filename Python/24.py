# Short Question Description: What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# Author: @SelimGunal
# not Finished on 16.07.2023

import copy

theString = ["A", "B", "C"]
fixed = -1
remain = 4

def permutation(theString, fixed, remain):
    fixed += 1
    remain -= 1
    cache = theString[fixed]


    # print(theString[0:fixed])

    if remain == 1:
        print(theString)
        return None

    for i in range(fixed, len(theString)):
        cacheString = copy.copy(theString)

        cacheString[fixed] = cacheString[i]
        cacheString[i] = cache
        permutation(cacheString, fixed, remain)



permutation(theString, fixed, remain)
