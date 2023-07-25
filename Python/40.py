# first create the number than find all the d1 * d10
# d represents the digit for eg 23456 what is d3 = 4

theString = ""
i = 1
# this thile loop creates string that combines i for eg i is "4" and the string is "123" it makes "1234"
while len(theString) <= 1000000:
    theString = theString + str(i)
    i += 1

i = 1
result = 1
# this while loop is just theString[10] * theString[100] ...
while i <= 1000000:
    # we must get i-1 because in python string starts with 0
    result = result * int(theString[i-1])
    i = i * 10

# expected result 210
print(result)
