if isPentagonal(pentagonalK):
    pentagonalNumbers.append(pentagonalK)
    print(pentagonalK)
    for x in range(0, len(pentagonalNumbers) - 1):
        if isPentagonal(pentagonalK - pentagonalNumbers[x]) and isPentagonal(pentagonalK + pentagonalNumbers[x]):
            result = pentagonalK - pentagonalNumbers[x]
            loop = False

pentagonalK += 1
