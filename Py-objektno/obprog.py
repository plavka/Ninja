# -*- coding: utf-8 -*-

class user(object):
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

korisnik = user("Darko", "Tomislav")
marko = user("Marko", "Ivezic")
iva = user("Iva", "Ivkovic")
korisnici = [
    korisnik,
    marko,
    iva
]
for useri in korisnici:
    print "Naš korisnik se zove " + useri.ime + " " + useri.prezime


