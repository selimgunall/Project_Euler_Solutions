# finished# Short Question Description: What is the sum of the digits of the number 2 ** 1000
# # Author: @SelimGunal
# # Finished on 25.06.2023

theNumber = str(2 ** 1000)

sum = 0
for i in range(0, len(theNumber)):
    sum = sum + int(theNumber[i])

print(sum)

# output: 1366
