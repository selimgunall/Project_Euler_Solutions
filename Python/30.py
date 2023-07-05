# Short Question Description: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
# Author: @SelimGunal
# Finished on 05.07.2023

result = 0
for i in range(2, 900000):
    strI = str(i)
    sum = 0
    for x in range(0, len(strI)):
        sum += int(strI[x]) ** 5

    if sum == i:
        result += i
        print(i)

print()
print(result)

