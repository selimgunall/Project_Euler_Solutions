#finding a numbers divisors

theNumber = 220
sum = 0
for x in range(1, theNumber):
    if (theNumber % x == 0):
        sum = sum + x

print(sum)
