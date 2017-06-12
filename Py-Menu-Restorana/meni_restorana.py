# -*- coding: utf-8 -*-

print "Dobrodošli u restoran."

menu = {}

while True:
    naziv_hrane = raw_input("Upišite naziv hrane: ")
    cijena_hrane = raw_input("Unesite cijenu za '%s': " % naziv_hrane)
    menu[naziv_hrane] = cijena_hrane

    new = raw_input("Da li želite dodati još jedno jelo? (da/ne) ")

    if new.lower() == "ne":
        break

print "Menu: %s" % menu

with open("menu.txt", "w+") as menu_file:
    for hrana in menu:
        menu_file.write("%s, %s kn\n" % (hrana, menu[hrana]))

print "Doviđenja!"
