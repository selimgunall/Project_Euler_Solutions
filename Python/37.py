# Short Question Description: Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# Author: @SelimGunal
# Finished on 23.07.2023

import math

def isPrime(whatNumber):
    x = 2
    while x <= int(math.sqrt(whatNumber)) + 1:
        if (whatNumber % x == 0 and whatNumber != 2) or whatNumber == 1:
            return 0
        x += 1
    return 1

result = 0
whatNumber = 8
truncatable = 0
while truncatable < 11:

    if isPrime(whatNumber):
        strCurrentN = str(whatNumber)
        lenStrCurrentN = len(strCurrentN)

        truncatableListR = []
        truncatableList = []
        isTruncatable = True
        for z in range(len(strCurrentN)-1, -1, -1):
            truncatableListR.insert(0, strCurrentN[z])
            truncatableList.append(strCurrentN[lenStrCurrentN-z-1])

            intListR = int("".join(truncatableListR))
            intList = int("".join(truncatableList))

            if not(isPrime(intListR)) or not(isPrime(intList)):
                isTruncatable = False

        if isTruncatable:
            truncatable += 1
            result += whatNumber

    whatNumber = whatNumber + 1

# expected answer 748317
print(result)
