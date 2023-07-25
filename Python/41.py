# make a while loop that prints pandigital prime number when it has found

import math

# this checks if a number is pandigital and 9 digit
def isPandigital(number):
    strNumber = str(number)
    for i in range(len(strNumber), 0, -1):
        if not(str(i) in strNumber):
            return 0

    # if the number is not 9 digits it is not condicered to be a pandigital
    if len(strNumber) != 9:
        return 0
    return 1

# this function checks if provided number is prime
def isPrime(number):
    for divisor in range (int(math.sqrt(number)) + 1, 1, -1):
        if number % divisor == 0 and number != 2:
            return False
    return True

i = 2
while True:
    if isPrime(i):
        if isPandigital(i):
            print(i)
    i += 1
