
def isPandigital(number):
    strNumber = str(number)
    for i in range(9, 0, -1):
        if not(str(i) in strNumber):
            return 0

    if len(strNumber) != 9:
        return 0
    return 1


for z in range(1, 10000):

    currentPandigital = ""
    for i in range(1, (9 // len(str(z))) + 1):
        currentPandigital = currentPandigital + str(z * i)

    if isPandigital(currentPandigital):
        print(currentPandigital)