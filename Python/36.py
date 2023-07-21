# Short Question Description: Find the sum of all numbers, less than one million, which are palindromic in base 10 and base.
# Author: @SelimGunal
# Finished on 21.07.2023

result = 0
for i in range(1, 1000000):
    binNumber = str(bin(i))[2:]
    strI = str(i)

    if strI[::-1] == strI and binNumber == binNumber[::-1]:
        result += i

print(result)
