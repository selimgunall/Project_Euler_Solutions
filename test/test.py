zort = """
ali
ata
bak
"""

z = 0
for i in range(1, len(zort), 4):
    print(zort[i:i+3])
    z += 3
print(z)
