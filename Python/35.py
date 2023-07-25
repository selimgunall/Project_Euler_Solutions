# first create a for loop that goes until 1000000
# than check if that number is prime
# after that check all rotations if they are prime than add to a list the main number
# we can find all rotations by changing the numbers first element to the last see test/35.py

# How many circular primes are there below one million?

import math

#
# number = 1019
# listNumber = []
# while number != 0:
#     result.append(number % 10)
#     number = number // 10

# this function checks if provided number is prime
def isPrime(number):
    for divisor in range (int(math.sqrt(number))+1, 1):
        if number % divisor == 0:
            return 0
    return 1


# it slides the list bor eg. from 197 to 971
def slideList(theNumber):
    cache = theNumber[0]
    theNumber.pop(0)
    theNumber.append(cache)


for i in range(2, 1000000):
    if isPrime(i):
        pass
