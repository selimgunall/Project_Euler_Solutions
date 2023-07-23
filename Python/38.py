# Short Question Description: What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ..., n) where n > 1 ?
# Author: @SelimGunal
# Finished on 24.07.2023

# this checks if a number is pandigital and 9 digit
def isPandigital(number):
    strNumber = str(number)
    for i in range(9, 0, -1):
        if not(str(i) in strNumber):
            return 0

    # if the number is not 9 digits it is not condicered to be a pandigital
    if len(strNumber) != 9:
        return 0
    return 1

# the question wantes n to be bigger than 1 so maximum maximum is 1000020000
# 10000 is the limit because 1000020000 (10000*1  10000*2) is 10 digit
for z in range(1, 10000):

    currentPandigital = ""
    for i in range(1, (9 // len(str(z))) + 1):
        # makes a pandigital number
        currentPandigital = currentPandigital + str(z * i)

    if isPandigital(currentPandigital):
        result = currentPandigital

print(result)
