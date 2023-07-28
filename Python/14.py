# Short Question Description: Which starting number, under one million, produces the longest chain?
# https://projecteuler.net/problem=14
# Author: @SelimGunal
# Finished on 23.06.2023

counter = 0
biggestCounter = 0
for y in range(1, 1000000 + 1):
    x = y
    counter = 1
    while (x != 1):
        if ((x % 2) == 0):
            x = x / 2
        else:
            x = (3 * x) + 1
        counter = counter + 1
        # print(x)

    # print(counter)

    if(counter > biggestCounter):
        biggest = y
        biggestCounter = counter

print(biggest)
print("finished")

# output: 837799
