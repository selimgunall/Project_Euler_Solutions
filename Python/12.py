# Short Question Description: What is the value of the first triangle number to have over five hundred divisors?
# Author: @SelimGunal
# finished on 02.02.2023
#https://www.mathsisfun.com/algebra/triangular-numbers.html
#The logic is you sum all numberzs to a end point like if we give 4th triangle as an example 1 + 2 + 3 + 4 = 10

import math

divisors = 0
triangle = 1
bottom = 1
while divisors < 500:
    triangle = triangle + bottom + 1
    bottom += 1
    divisors = 0
    for i in range(1, int(math.sqrt(triangle))+1):
        if triangle % i == 0:
            divisors += 2



print(triangle)
print(divisors)

