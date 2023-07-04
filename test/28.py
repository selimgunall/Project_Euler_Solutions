
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
for i in range(1, 1002002):
    if i==x or i==y or i==z or i==t:
        if i==x or i==y:
            if i==x:
                sum += i
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


print(sum+1)
