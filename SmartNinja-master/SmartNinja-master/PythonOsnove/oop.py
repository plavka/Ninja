class user(object):
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
    def puno_ime(self):
        return self.ime + " " + self.prezime
class nas_korisnik(user):
    def __init__(self, ime, prezime, broj_telefona):
        user.__init__(self, ime, prezime)
        self.broj_telefona = broj_telefona
        print self.telefon()
    def telefon(self):
        return "Broj telefona je: " + self.broj_telefona

novi_korisnik = nas_korisnik("Imerdf","Prezimefgds", "99643432")
print novi_korisnik.puno_ime()
print novi_korisnik.telefon()

korisnik = user("Ivan", "Ijfkdhsg")
marko = user("Marko", "dhaf")
iva = user("Iva", "fdsg")
korisnici = [
    korisnik,
    marko,
    iva
]
for usr in korisnici:
    print "Nas korisnik se zove " + usr.puno_ime()

