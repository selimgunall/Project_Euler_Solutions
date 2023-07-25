number = [2,9]

cache = number[0]
number.pop(0)
number.append(cache)

import math

def isPrime(number):
    for divisor in range (int(math.sqrt(number))+1, 1,-1):
        if number % divisor == 0 and number != 2:
            return False
    return True

print(isPrime(4))

