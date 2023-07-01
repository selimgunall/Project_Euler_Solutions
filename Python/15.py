# Short Question Description: How many such routes are there through a 20 x 20 grid?
# Author: @SelimGunal
# Finished on 24.06.2023

# https://www.youtube.com/watch?v=wc1hZpDPQFA
# https://stemhash.com/counting-lattice-paths/
# n choose k
# n is how much you can move k is x

def makeFact(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result

# (k, n)
x = 20
y = 40

factY = makeFact(y)
y_minus_x_fact = makeFact(y-x)
factX = makeFact(x)

result = factY / (y_minus_x_fact * factX)
print(result)

# output: 137846528820
