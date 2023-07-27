# first add pentagonal that you found and than substract the smaller numbers in the list for eg i am at 35 and removing 22 and testing if the result is pentagonal
# that is all

def isPentagonal(number):
    n = 1
    currentPentagonal = 1
    while currentPentagonal < number:
        currentPentagonal = (n * (3 * n - 1)) / 2
        n += 1

    if currentPentagonal == number:
        return True
    return False

def generatePentagonal(n):
    return (n * (3 * n - 1)) // 2

n = 1
pentagonalNumbers = []
loop = True
while loop:
    currentPentagonal = generatePentagonal(n)
    for i in range(0, len(pentagonalNumbers)):
        if isPentagonal(currentPentagonal - pentagonalNumbers[i]):
            if isPentagonal(currentPentagonal + pentagonalNumbers[i]):
                print(currentPentagonal - pentagonalNumbers[i])
                loop = False

    pentagonalNumbers.append(currentPentagonal)
    n += 1

print(result)
