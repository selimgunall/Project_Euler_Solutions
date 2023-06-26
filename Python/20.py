# Short Question Description: Find the sum of the digits in the number 100!
# Author: @SelimGunal
# Finished on 26.06.2023
def generateFactioral(number):
    sum = 1
    for i in range(number, 0, -1):
        sum = sum * i
    return sum

theNumber = str(generateFactioral(100))

sum = 0
for i in range(0, len(theNumber)):
    sum = sum + int(theNumber[i])


print(sum)

