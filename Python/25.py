
x = 1
y = 1
sum = 0
while 1000>x or 1000>y or 1000>sum:
    sum = x + y
    x = sum + y
    y = sum + x

print(x)
print(y)
print(sum)
