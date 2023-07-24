# right angled triangle is "dik ucgen" in turkish
# perimeter is "cevre" in turkish
# temel bir while loop olacak p 1000den kucuk oldugu surece calisacak (a**2 + b**2  =  c**2) (a+b+c = p)
# while loopun icinde iki tane for loop olacak birise a digeri b icin bunlarin karlerinin toplami kalan sayini karesine esit olcak
# b loopu a-120 ye kadar gidecek

# Short Question Description: For which value of p <= 1000, is the number of solutions maximised?
# Author: @SelimGunal
# Finished on 24.07.2023

# For which value of p <= 1000, is the number of solutions maximised?

import math
p = 1

biggestS = 0
# question wants perimeter to maximum to be 1000
while p <= 1000:
    currentSolutionN = 0

    # a length side
    for a in range(1, p):
        # b length side this goes until p-a+1 because for example p=1000 and a = 998 so b must maximum be 2
        for b in range(a, p - a + 1):

            sqrtAandB = math.sqrt(a**2 + b**2)

            # this gives us c
            pMinusAandB = p - a - b

            # in this if loop we are going to try if sqrt of (p - (a + b)) equals c
            if sqrtAandB == pMinusAandB:
                currentSolutionN += 1

    # this makes the biggest perimeter
    if currentSolutionN > biggestS:
        biggestS = currentSolutionN
        biggestP = p

    p += 1

# expected print is 840 in about 30 seconds
print(biggestP)
