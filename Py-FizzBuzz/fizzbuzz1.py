# -*- coding: utf-8 -*-
#korisnik mora izabrati broj izmedu 1 i 100

while True:
    unos = int(raw_input("Unesite broj između 1 i 100"))
    if unos > 0 and unos < 101:
        break
    else:
        print("Uneseni broj nije između 1 i 100")
print unos
#ispisati brojeve od 1 do unesenog broja
for broj in range(1, (unos+1)):
    if broj % 3 == 0 and broj % 5 == 0:
        print "fizzbuzz"
    elif broj % 3 == 0:
        print "fizz"
    elif broj % 5 == 0:
        print "buzz"
    else:
        print broj
