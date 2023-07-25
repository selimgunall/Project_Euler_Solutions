# make a while loop that prints pandigital prime number when it has found
# this question is nonsense because there is no limit you can i think find 9 digit pandigital that is prime but that requires the many computer power to find
# this is really optimized solution

# Short Question Description: What is the largest n-digit pandigital prime that exists?
# Author: @SelimGunal
# Finished on 25.07.2023

import math

# this checks if a number is pandigital
def isPandigital(number):
    strNumber = str(number)
    for i in range(len(strNumber), 0, -1):
        if not(str(i) in strNumber):
            return 0
    return 1

# this function checks if provided number is prime
def isPrime(number):
    for divisor in range(int(math.sqrt(number)) + 1, 1, -1):
        if number % divisor == 0 and number != 2:
            return False
    return True

i = 8000000
while True:
    if isPrime(i):
        if isPandigital(i):
            print(i)
    i -= 1

# expected answer 7652413
