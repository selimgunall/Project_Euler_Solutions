# Short Question Description: What is the value of the first triangle number to have over five hundred divisors?
# Author: @SelimGunal
# tried on 21.06.2023
#https://www.mathsisfun.com/algebra/triangular-numbers.html
#The logic is you sum all numberzs to a end point like if we give 4th triangle as an example 1 + 2 + 3 + 4 = 10

import math

divisors = 0
x = 10
while x < 5000000:
    theNumber = x
    divisors = 0
    x = theNumber
    for i in range(int(math.sqrt(theNumber))+1, 0, -1):
        if theNumber % i == 0:
            divisors += 2



    x += 1
print(x)
print(divisors)

