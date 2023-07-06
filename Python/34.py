
for z in range
    number = "145"
    intNumber = int(number)
    sum = 0
    for i in range(0, len(number)):
        current = int(number[i])

        # make fact
        currentSum = 1
        for x in range(1, current+1):
            currentSum *= x

        sum += currentSum

    if sum == intNumber:
        print(intNumber)
