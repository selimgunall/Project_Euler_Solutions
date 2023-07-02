# Short Question Description: What is the index of the first term in the Fibonacci sequence to contain digits?
# Author: @SelimGunal
# finished on 02.07.2023

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

