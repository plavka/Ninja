#Unos podataka
a = input("Unesi prvi broj: ")
b = input("Unesi drugi broj: ")
operator = raw_input("Unesi operator: ")
#Operacije + - * /
rezultat = True
if operator == "+":
    rezultat = a + b
elif operator == "-":
    rezultat = a - b
elif operator == "*":
    rezultat = a * b
elif operator == "/":
    rezultat = a / b
else:
    rezultat = False
    print("Operator mora biti jedan od znakova: + - * /")
#Ispis podataka 11 + 11
if rezultat != False:
    print(str(a) + " " + operator + " " + str(b) + " = " + str(rezultat))
