numbers = []

for i in range(2, 101):
    for x in range(2, 101):
        currentNumber = str(i**x)

        if not(currentNumber in numbers):
            numbers.append(currentNumber)

print(len(numbers))
