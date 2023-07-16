import math

for x in range(0, 1000000):

    i = 1

    isPrime = True

    while isPrime == True and i < math.sqrt(x):
        if x % i == 0:
            isPrime = False
        i += 1

    if isPrime == True:
        print(x)