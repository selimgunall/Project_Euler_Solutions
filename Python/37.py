
import math

while truncatable <= 11:
    pass


whatNumber = 2
truncatable = 0
while truncatable <= 11:
    for x in range(2, int(math.sqrt(whatNumber))+1):
        indicator = 0
        if whatNumber % x == 0:
            indicator = 1
            break
    if indicator == 0:
        pass
        # my code
    whatNumber = whatNumber + 1


