# -*- coding: utf-8 -*-
import random


def main():
    secret = random.randint(1, 30)

    while True:
        guess = int(raw_input("Pogodi tajni broj (između 1 i 30): "))

        if guess == secret:
            print "Pogodio si - čestitam! Tajni broj je %s :)" % secret
            break
        elif guess > secret:
            print "Žao mi je, tvoj broj je prevelik... Pokušaj ponovo."
        elif guess < secret:
            print "Žao mi je, tvoj broj je premali... Pokušaj ponovo."


if __name__ == "__main__":
    main()