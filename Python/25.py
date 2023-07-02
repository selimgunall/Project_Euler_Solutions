
x = 1
y = 1
sum = 0
count = 0
while 1000>len(str(x)) and 1000>len(str(y)) and 1000>len(str(sum)):
    sum = x + y
    x = sum + y
    y = sum + x
    count += 3

print(count)

