# Short Question Description: Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Author: @SelimGunal
# Finished on 06.07.2023

result = 0
for z in range(3, 200000):
    number = str(z)
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
        result += intNumber

print(result)
