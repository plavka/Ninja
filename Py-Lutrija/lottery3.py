import random
lotterynumbers = []
x = 0

while x < 7:
    lotterynumbers.append(random.randint(1, 49))
    x += 1

lotterynumbers.sort()
print lotterynumbers