
import math

def isPrime(whatNumber):
    for x in range(2, int(math.sqrt(whatNumber))+1):
        indicator = 0
        if whatNumber % x == 0:
            return 1
    return 0


whatNumber = 2
truncatable = 0
while truncatable <= 11:

    if isPrime(whatNumber) == 0:
        strCurrentN = str(whatNumber)
        lenStrCurrentN = len(strCurrentN)

        truncatableListR = []
        truncatableList = []
        for z in range(len(strCurrentN)-1, -1, -1):
            truncatableListR.insert(0, strCurrentN[z])
            truncatableList.append(strCurrentN[lenStrCurrentN-z-1])



    whatNumber = whatNumber + 1
