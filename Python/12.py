# Short Question Description: !!!
# Author: @SelimGunal
# Finished on !!!
#https://www.mathsisfun.com/algebra/triangular-numbers.html
#The logic is you sum all numberzs to a end point like if we give 4th triangle as an example 1 + 2 + 3 + 4 = 10

from threading import Thread

# def generateTriangle(number):
#     whichNumber = number
#     triangle = 0
#     for i in range(1, whichNumber + 1):
#         triangle = triangle + i
#     return triangle

# def checkDivisors(triangle):
#     i = 1
#     count = 0
#     while(triangle >= i):
#         if((triangle % i) == 0):
#             count = count + 1
#         i = i + 1
#
#     if (count >= 500):
#         print(triangle)
#     return count

def allFunc(number):
    whichNumber = number
    triangle = 0
    for i in range(1, whichNumber + 1):
        triangle = triangle + i
    #return triangle

    i = 1
    count = 0
    while (triangle >= i):
        if ((triangle % i) == 0):
            count = count + 1
        i = i + 1

    if (count >= 500):
        print(triangle)
    return count

number = 1
while (True):
    theFunc = Thread(target=allFunc, args=[number])
    theFunc.start()
    number = number + 1

