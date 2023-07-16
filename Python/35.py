import math

# Short Question Description: !!!
# Author: @SelimGunal
# Finished on !!!
whatNumber = 2
primeNumbersList = []
indicator = 0

while whatNumber < 1000000:
    for x in range (2 ,int(math.sqrt(whatNumber))+1):
        indicator = 0
        if (whatNumber % x == 0):
            indicator = 1
            break
    if (indicator == 0):
        primeNumbersList.append(whatNumber)
        print(whatNumber)
    whatNumber = whatNumber + 1
# print(primeNumbersList)
#The result is