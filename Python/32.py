# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# multiplicand = carpilan
# multiplier = carpan

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
for product in range(1, 10000):
    for multiplicand in range(1, int(math.sqrt(product))+1):
        if product % multiplicand == 0:
            multiplier = int(product / multiplicand)

            if isPandigital(str(product) + str(multiplier) + str(multiplicand)):
                if not(product in result):
                    result.append(product)

sum = 0
for x in range(0, len(result)):
    sum += result[x]

print(sum)
