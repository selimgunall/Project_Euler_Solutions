
import math

def isPrime(whatNumber):
    for x in range(2, int(math.sqrt(whatNumber))+1):
        indicator = 0
        if whatNumber % x == 0:
            return 0
    return 1


whatNumber = 8
truncatable = 0
while truncatable <= 11:

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


    whatNumber = whatNumber + 1
