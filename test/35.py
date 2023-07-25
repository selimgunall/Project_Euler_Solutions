number = [1,9,7]

cache = number[0]
number.pop(0)
number.append(cache)

print(number)

