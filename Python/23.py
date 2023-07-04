
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

sumNumbers = {}
for i in range(1, 28123):
    sumNumbers[i] = i
    sumNumbers

print("basladi")

# sum 28122 den kucuk oldugu surece while dongusu yap
# for i in range(0, len(abundant)):
#     if i + i > 28123:
#         break
#     for x in range(i, len(abundant)):
#         sum = abundant[i] + abundant[x]
#         sumNumbers[sum-1] = 0

i = 0
x = i
sum = 0
while i < len(abundant):
    x = i
    sum = 0
    while sum < 28123:
        sum = abundant[i] + abundant[x]
        sumNumbers[sum] = 0
        x += 1

    print(sumNumbers[i + 1])


    i += 1



for i in range(1, 28123):
    print(sumNumbers[i])

print("bitti")


sum = 0
for i in range(1, 28123):
    sum = sum + sumNumbers[i]

print(sum)
