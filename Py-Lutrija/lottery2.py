from random import randint as rand_number

def create_lottery_numbers(amount=7):
    return [rand_number(1,49) for i in range(amount)]

def get_user_input(prompt="Please enter how many random numbers would you like to have: "):
    return int(input(prompt))

a = get_user_input()

for i in range(a):
    create_lottery_numbers()

