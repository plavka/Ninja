import random
baza = {
    "hrvatska": "zagreb",
    "slovenia": "ljubljana",
    "austria": "bec"
}
def glavni_grad(drzava, grad):
    for key in baza:
        if baza[key] == grad and key == drzava:
            return True
    return False
def main():
    while True:
        rand = random.randint(0, 2)
        drzava = sorted(baza.keys())[rand]
        grad = raw_input("Kako se zove glavni grad za drzavu %s: " % drzava)
        if glavni_grad(drzava, grad):
            break
    print "Bravo odgovor je tocan!"
if __name__ == "__main__":
    main()