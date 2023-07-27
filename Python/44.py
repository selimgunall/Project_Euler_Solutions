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

pentagonalK = 1
pentagonalNumbers = []
loop = True
while loop:
    if isPentagonal(pentagonalK):
        pentagonalNumbers.append(pentagonalK)

        for x in range(0, len(pentagonalNumbers) - 1):
            if isPentagonal(pentagonalK - pentagonalNumbers[x]) and isPentagonal(pentagonalK + pentagonalNumbers[x]):
                result = pentagonalK - pentagonalNumbers[x]
                loop = False

    pentagonalK += 1

print(result)
