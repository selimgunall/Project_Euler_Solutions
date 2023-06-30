theNumber = list(str(1/7))

theNumber.pop(0)
theNumber.pop(0)
user = "".join(theNumber)

isFinished = False

longest = 0
for i in range(0, len(user)):
    text = user[i]
    for x in range(i + 1, len(user)):
        if not (user[x] in text):
            text = text + user[x]
        else:
            if len(text) > longest:
                longest = len(text)
                longestText = text
            break
        # When this for loop finishes it continues with outer for loop that's why we should make a isFinished
        if x == len(user) - 1:
            isFinished = True

    if isFinished:
        break

print(longest)
print(longestText)

