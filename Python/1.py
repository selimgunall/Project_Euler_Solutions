#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

# Short Question Description: !!!
# Author: @SelimGunal
# Finished on !!!

sum = 0

#I've done a for loop because the the question wants the numbers below the one thousand
for i in range(0 ,1000):
    if (i % 3 == 0 or i % 5 == 0):
        sum = sum + i
print(sum)
#The result is 233168
