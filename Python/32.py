# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# multiplicand = carpilan(in turkish)
# multiplier = carpan(in turkish)

import math

# this my function to check if a number is pandigital
def isPandigital(number):
    strNumber = str(number)
    for i in range(9, 0, -1):
        if not(str(i) in strNumber):
            return 0

    # if the number is not 9 digits it is not condicered to be a pandigital
    if len(strNumber) != 9:
        return 0
    return 1

result = []
# there is for loop because this is a limited situation because you might ask (1*10000=10000) it exceedes our 9 digit rule one digit only
for product in range(1, 10000):
    # first we must find multiplicand after i found multiplicand then find the multiplier because it is much faster
    # also the code goes until the squareroot of the number then find the multiplicand multiplier
    for multiplicand in range(1, int(math.sqrt(product))+1):
        if product % multiplicand == 0:
            multiplier = int(product / multiplicand)

            # this if checkes if the number is pandigital
            if isPandigital(str(product) + str(multiplier) + str(multiplicand)):
                if not(product in result):
                    result.append(product)

sum = 0
# this sums up the numbers in the list
for x in range(0, len(result)):
    sum += result[x]

# expected output 45228
print(sum)
