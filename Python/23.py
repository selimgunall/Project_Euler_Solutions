

perfect = []
abundant = []
for x in range(1, 28123):


    theNumber = x
    sum = 0
    for i in range(1, theNumber):
        if theNumber % i == 0:
            sum += i
    # print(sum)

    if sum >= theNumber:
        if sum == theNumber:
            perfect.append(sum)
        else:
            abundant.append(theNumber)

print(perfect)
print(abundant)

sumOfTwo = []
for i in range(0, len(abundant)):
    for x in range(i, len(abundant)):
        sumOfTwo.append(i+x)

sumOfTwo.sort()

result = 0
for i in range(0, len(sumOfTwo)):
    if not(i in sumOfTwo):
        result += i
