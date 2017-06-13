from random import randint

NewNumber = 0
Lottery = []
MyNumbers = []
RightNumbers = 0

while(len(Lottery) < 7):
    NewNumber = randint(1,49)
    if(NewNumber not in Lottery):
        Lottery.append(NewNumber)

while(len(MyNumbers) < 7):
    NewNumber = raw_input("Please write your number between 1-49: ")
    if(NewNumber not in MyNumbers and (NewNumber <= 49 or NewNumber > 0)):
        MyNumbers.append(NewNumber)

for number in Lottery:
    for myNumber in MyNumbers:
        if(number == myNumber):
            RightNumbers += 1

print "You have " +str(RightNumbers) + " right numbers:!"
print "The lottery numbers were: "
print Lottery

