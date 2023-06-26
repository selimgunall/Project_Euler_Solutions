# Short Question Description: !!!
# Author: @SelimGunal
# Finished on !!!
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

