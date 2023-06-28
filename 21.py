
numsList = {}
for i in range(1, 10000):

    sum = 0
    for x in range(1, i):
        if (i % x == 0):
            sum = sum + x

    numsList[i] = sum

# print(numsList[20])

# make a nested for loop for to contrast the numbers

