# Short Question Description: Find the sum of all the primes below two million.
# Author: @SelimGunal
# Finished on 28.07.2023

import math

# this function checks if provided number is prime
def isPrime(whatNumber):
    x = 2
    while x <= int(math.sqrt(whatNumber)) + 1:
        if (whatNumber % x == 0 and whatNumber != 2) or whatNumber == 1:
            return 0
        x += 1
    return 1

i = 1
result = 0
while i < 2000000:
    if isPrime(i):
        result += i
    i += 1

#The result is142913828922 in 45 seconds
print(result)
