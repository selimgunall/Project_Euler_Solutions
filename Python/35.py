
# Short Question Description: !!!
# Author: @SelimGunal
# Finished on !!!


import math

def permutation(theString, fixed, remain):
    remain -= 1

    if remain:
        numbers.append("".join(theString))
        return None

    fixed += 1
    cache = theString[fixed]

    for i in range(fixed, len(theString)):
        cacheString = theString[:]

        cacheString[fixed] = cacheString[i]
        cacheString[i] = cache
        permutation(cacheString, fixed, remain)


whatNumber = 2
primeNumbersList = []
indicator = 0

while whatNumber < 1000000:
    for x in range (2 ,int(math.sqrt(whatNumber))+1):
        indicator = 0
        if (whatNumber % x == 0):
            indicator = 1
            break
    if (indicator == 0):
        primeNumbersList.append(whatNumber)
    whatNumber = whatNumber + 1

print("bitti")

result = 0

for x in range(0, len(primeNumbersList)):
    numbers = []
    theString = list(str(primeNumbersList[x]))
    fixed = -1
    remain = len(theString)

    permutation(theString, fixed, remain)
    numbers.sort()

    isCircularPrimes = True

    for z in range(0, len(numbers)):
        if not(int(numbers[z]) in primeNumbersList):
            isCircularPrimes = False
            break

    if isCircularPrimes:
        result += 1






print(result)
#The result is