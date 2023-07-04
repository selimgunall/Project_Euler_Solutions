# Short Question Description: What is the sum of the numbers on the diagonals in a 1000 by 1000 spiral formed in the same way?
# Author: @SelimGunal
# Finished on 04.07.2023
# there is a picture

x=3
y=5
z=7
t=9
rise  = 8

riseX = 2
riseY = 4
riseZ = 6
riseT = 8

sum = 0

# checkes all the numbers from 1 to 1002001(1001*1001)
for i in range(1, 1002002):
    # this one if is pratic because there is only one if if the number is not in a diagonals
    if i==x or i==y or i==z or i==t:
        if i==x or i==y:
            if i==x:
                sum += i
                # there was a problem if a do this x += rise + 2 because there is only on two at the beginning then it continues with 8 if i do earlier it generates 10
                riseX += rise
                x += riseX
            else:
                sum += i
                riseY += rise
                y += riseY

        else:
            if i == z:
                sum += i
                riseZ += rise
                z += riseZ
            else:
                sum += i
                riseT += rise
                t += riseT


# we add one because at first we don't count 1
print(sum+1)

# output: 669171001
