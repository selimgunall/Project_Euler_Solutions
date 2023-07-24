import math
p = 1


p = 120
# a length side
for a in range(1, p):
    # b length side this goes until p-a+1 because for example p=1000 and a = 998 so b must maximum be 2
    for b in range(1, p - a + 1):

        sqrtAandB = math.sqrt(a**2 + b**2)

        # this gives us c
        pMinusAandB = p - a - b

        # in this if loop we are going to try if sqrt of (p - (a + b)) equals c
        if sqrtAandB == pMinusAandB:
            print(a, b, pMinusAandB)

