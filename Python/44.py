# first add pentagonal that you found and than substract the smaller numbers in the list for eg i am at 35 and removing 22 and testing if the result is pentagonal

# Short Question Description: Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = Pj - Pk is minimised; what is the value of D?
# Author: @SelimGunal
# Finished on 28.07.2023

# this function testes if the number is pentagonal by going every pentagonal numbers
def isPentagonal(number):
    n = 1
    currentPentagonal = 1
    while currentPentagonal < number:
        currentPentagonal = (n * (3 * n - 1)) // 2
        n += 1

    if currentPentagonal == number:
        return True
    return False

# this functions generates pentagonal number by n
def generatePentagonal(n):
    return (n * (3 * n - 1)) // 2

n = 1
pentagonalNumbers = []
loop = True
# this while loop generates pentagonal numbers by n and then checkes is the sum and abstracts are pentagonal
while loop:
    currentPentagonal = generatePentagonal(n)
    for i in pentagonalNumbers:
        # this if loop abstracts and then checkes if result is in pentagonalNumbers eg. 12-5=7 this is not in the list
        if currentPentagonal - i in pentagonalNumbers:

            # in this loop it checes by trying all pentagonal numbers becuse in previous if it checks by abstract but there is no way in sum
            if isPentagonal(currentPentagonal + i):
                result = currentPentagonal - i
                loop = False
                break

    pentagonalNumbers.append(currentPentagonal)
    n += 1

# expected result 5482660
print(result)
