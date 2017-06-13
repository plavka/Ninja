# -*- coding: utf-8 -*-

class user(object):
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def puno_ime(self):
        return self.ime + " " + self.prezime

class nas_korisnik(user):
    def __init__(self, ime, prezime, broj_telefona):
        user.__init__(self, ime, prezime,)
        self.broj_telefona = broj_telefona
        print self.telefon()
    def telefon(self):
        return "Broj telefona je: " + self.broj_telefona

novi_korisnik = nas_korisnik("Milko", "Safar", "091569872")
print novi_korisnik.ime #mogli bi staviti umjesto ime i prezime i useri.puno_ime()
print novi_korisnik.prezime
print novi_korisnik.broj_telefona #tu mozemo staviti i novi_korisnik.telefon()

korisnik = user("Darko", "Tomislav")
marko = user("Marko", "Ivezic")
iva = user("Iva", "Ivkovic")
korisnici = [
    korisnik,
    marko,
    iva
]
for useri in korisnici:
    print "Naš korisnik se zove " + useri.puno_ime()



