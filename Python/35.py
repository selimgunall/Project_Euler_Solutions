
# Short Question Description: !!!
# Author: @SelimGunal
# Finished on !!!

import math


whatNumber = 2
primeNumbersList = []
indicator = 0

while (whatNumber < 2000000):
    for x in range (2, int(math.sqrt(whatNumber))+1):
        indicator = 0
        if (whatNumber % x == 0):
            indicator = 1
            break
    if (indicator == 0):
        primeNumbersList.append(whatNumber)
    whatNumber = whatNumber + 1

# sayilari bir birim sola kaydir

print("bitti")

for i in range(0, len(primeNumbersList)):
    theNumber = []
    strNumber = str(primeNumbersList[i])
    for x in range(len(strNumber)-1, -1, -1):
        theNumber.insert(0, strNumber[x])


    tempList = theNumber[:]









#The result is