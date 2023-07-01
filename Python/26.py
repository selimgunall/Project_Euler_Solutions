# Short Question Description: Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# Author: @SelimGunal
# tried on 30.06.2023

devir = "123123123"

biggestDevir = ""
text = devir[0]
for i in range(0, len(devir)):
    if text[0] == devir[i]:
        round = 0
        count = 0
        for x in range(i, len(devir)):
            if round == len(text):
                if round > len(biggestDevir):
                    biggestDevir = text
                break

            if text[round] == devir[x]:
                count += 1

            round = round + 1

print(biggestDevir)

