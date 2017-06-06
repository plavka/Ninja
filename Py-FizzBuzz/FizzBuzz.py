#!/usr/bin/env python
# -*- coding: utf-8 -*-
#korisnik mora izabrati broj izmedu 1 i 100

print "Welcome to the fizzbuzz game!"

entry = raw_input("Please enter a number between 1 and 100: ")

try:
    entry = int(entry)

    for num in range(1, entry+1):
        if num % 3 == 0 and num % 5 == 0:
            print "fizzbuzz"
        elif num % 3 == 0:
            print "fizz"
        elif num % 5 == 0:
            print "buzz"
        else:
            print num
except Exception as e:
    print "Please enter a whole number."