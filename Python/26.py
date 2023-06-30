# Short Question Description: Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# Author: @SelimGunal
# tried on 30.06.2023

longestLongest = 0
for x in range(1, 1001):

    theNumber = list(str(1 / x))

    theNumber.pop(0)
    theNumber.pop(0)
    user = "".join(theNumber)

    isFinished = False
    longest = 0
    longestText = ""
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


    if longest > longestLongest:
        longestLongest = longest
        longestLongestNumber = x
        longestLongestText = longestText


print(longestLongestNumber)
print(longestLongestText)
