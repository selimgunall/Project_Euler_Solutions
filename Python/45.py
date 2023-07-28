# make a while loop that irritates n
# add all numbers that found with n to a list
# then for eg you are at n = 285 that mean you have already found P156 and H143 already added to the list

# Short Question Description: Find the next triangle number that is also pentagonal and hexagonal.
# Author: @SelimGunal
# Finished on 28.07.2023

# it generates triangle by number by n
def generateTriangle(n):
    return (n * (n + 1)) // 2

# it generates pentagonal number by n
def generatePentagonal(n):
    return (n * ((3 * n) - 1)) // 2

# it generates hexagonal number by n
def generateHexagonal(n):
    return n * ((2 * n) - 1)

pentagonalNumbers = []
hexagonalNumbers = []

loop = True
n = 1
# this while loop generates the numbers by n and then creates the numbers
# checks if current triangle number in other list it runs like this because for example you are at n = 285 that mean you have already found P156 and H143 already added to the list
while loop:
    currentTriangle = generateTriangle(n)

    if currentTriangle in hexagonalNumbers:
        if currentTriangle in pentagonalNumbers:
            result = currentTriangle

            if result > 40755:
                break

    pentagonalNumbers.append(generatePentagonal(n))
    hexagonalNumbers.append(generateHexagonal(n))

    n += 1

print(result)
