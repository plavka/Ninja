import random

lottery_numbers = []

for i in range (0,7):
    number = random.randint(1, 49)
    while number in lottery_numbers:
        number = random.randint(1,49)

    lottery_numbers.append(number)

lottery_numbers.sort()

print "Today's lottery numbers are: "
print (lottery_numbers)
