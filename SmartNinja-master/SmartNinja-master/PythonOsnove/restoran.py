jelovnik = {}
while True:
    naziv = raw_input("Naziv jela: ")
    cijena = raw_input("Cijena jela %s: " % naziv)
    jelovnik[naziv] = cijena
    if raw_input("Jos (da/ne): ") <> "da":
        break
dokument = open("jelovnik.txt", "w+")
for naziv in jelovnik:
    dokument.write(naziv + "  " + jelovnik[naziv] +"\n")
dokument.close()