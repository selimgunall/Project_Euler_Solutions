import math

p = 120
# a length side
for a in range(1, p):
    # b length side this goes until p-a+1 because for example p=1000 and a = 998 so b must maximum be 2
    # we are starting from a becuse while we are counting for the sum it reverses the number such as 20 40  to  40 20
    for b in range(a, p - a + 1):

        sqrtAandB = math.sqrt(a**2 + b**2)

        # this gives us c
        pMinusAandB = p - a - b

        # in this if loop we are going to try if sqrt of (p - (a + b)) equals c
        if sqrtAandB == pMinusAandB:
            print(a, b, pMinusAandB)
