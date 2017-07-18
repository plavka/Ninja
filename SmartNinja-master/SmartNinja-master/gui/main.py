from Tkinter import Tk, Button, Label, Entry
import tkMessageBox


window = Tk()
window.wm_title("Igra pogadanja")

#naraviti label s objasnjenjem
label = Label(window, text="Unesite broj")
label.pack()

#unos broja
entry = Entry(window)
entry.pack()

def button_press():
    try:
        unos =  int(entry.get())
        # obavjestit korisnika je li pogodio
        # ako ne reci je li broj veci ili manji
        odgovor = 32
        odgovor_tekst = ""
        if unos == odgovor:
            odgovor_tekst = "Tocno"
        elif odgovor < unos:
            odgovor_tekst = "Odgovor je manji od unesenog broja"
        else:
            odgovor_tekst = "Odgovor je veci od unesenog broja"

        tkMessageBox.showinfo("Rezultat", odgovor_tekst)
    except:
        tkMessageBox.showwarning("Greska", "Unos nije broj")

#pozvati provjeru
button = Button(window, text="Provjeri", command=button_press)
button.pack()


window.mainloop()
