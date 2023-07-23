
import math

def isPrime(whatNumber):
    # while ile yap
    for x in range(2, int(math.sqrt(whatNumber))+1):
        print()
        indicator = 0
        if whatNumber % x == 0 or whatNumber == 1:
            return 0
    return 1

print(isPrime(1))
