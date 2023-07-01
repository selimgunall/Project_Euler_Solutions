# Short Question Description: Evaluate the sum of all the amicable numbers under 10000.
# Author: @SelimGunal
# Finished on 29.06.2023

numsList = {}
for i in range(1, 10000):

    sum = 0
    for x in range(1, i):
        if (i % x == 0):
            sum = sum + x

    numsList[i] = sum


# print(numsList[220])

# make a nested for loop for to contrast the numbers

sum = 0
for i in range(1, 10000):
    for x in range(i+1, 10000):
        if((numsList[i] == x) and (numsList[x] == i)):
            sum = sum + i + x

print(sum)

# output: 31626
