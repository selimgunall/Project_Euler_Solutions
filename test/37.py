
import math

def isPrime(whatNumber):

    x = 2
    while x <= int(math.sqrt(whatNumber))+1:
        if (whatNumber % x == 0 and whatNumber != 2) or whatNumber == 1:
            return 0
        x += 1
    return 1

print(isPrime(3))
