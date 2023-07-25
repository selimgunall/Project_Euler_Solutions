# first create a for loop that goes until 1000000
# than check if that number is prime
# after that check all rotations if they are prime than add the main number to the list
# we can find all rotations by changing the numbers first element to the last see test/35.py

# Author: @SelimGunal
# Finished on 25.07.2023

# How many circular primes are there below one million?

import math

# this function checks if provided number is prime
def isPrime(number):
    for divisor in range (int(math.sqrt(number)) + 1, 1, -1):
        if number % divisor == 0 and number != 2:
            return False
    return True


# it slides the list bor eg. from 197 to 971
def slideList(theNumber):
    listNumber = list(theNumber)
    cache = listNumber[0]
    listNumber.pop(0)
    listNumber.append(cache)
    return "".join(listNumber)

circularPrimeList = []

for i in range(2, 1000000):
    if isPrime(i):
        isCircularPrime = True

        slided = str(i)
        # this for loop slides the slided int
        # is goes for to len(str(i)) - 1 because for example 197 we don't we don't need trice sliding twice is okay 197, 971, 719
        for z in range(0, len(str(i)) - 1):
            slided = slideList(slided)

            # if slided number is not prime breakes the loop
            if not(isPrime(int(slided))):
                isCircularPrime = False
                break

        if isCircularPrime:
            circularPrimeList.append(i)

print(len(circularPrimeList))


