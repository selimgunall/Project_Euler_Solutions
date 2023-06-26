# Short Question Description: !!!
# Author: @SelimGunal
# Finished on !!!
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

# x = 5
# while (x != 1):
#     if((x % 2) == 0):
#         x = x / 2
#     else:
#         x = (3 * x) + 1
#     print(x)


