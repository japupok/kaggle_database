import tkinter
from random import *

okno = tkinter.Tk()
okno.title("Hra NIM")
canvas = tkinter.Canvas(okno, width=400, height=200, bg="white")
canvas.pack()

# zakladne premene

pocet_zapaliek = randint(7,15) 
na_tahu = 1
reprizenka = []

stav = tkinter.StringVar()
stav.set(f"Hráč {na_tahu} je na ťahu.")

# funkcia na prekreslenie zapaliek
def vykresli(pocet=None):
    if pocet is None:
        pocet = pocet_zapaliek
    canvas.delete("all")
    for i in range(pocet):
        x = 20 + i * 20
        canvas.create_line(x, 100, x, 40, width=4, fill="orange")
        canvas.create_oval(x - 4, 30, x + 4, 40, fill="darkred")

# funkcia na tah hraca
def tah(pocet):
    global pocet_zapaliek, na_tahu
    if pocet_zapaliek > 0:
        if pocet <= pocet_zapaliek:
            pocet_zapaliek -= pocet
            reprizenka.append((na_tahu, pocet))
            if pocet_zapaliek == 0:
                stav.set(f"Hráč {na_tahu} prehral! Víťaz je hráč {3 - na_tahu}.")
                for b in tlacidla:
                    b.config(state="disabled")
                tlacidlo_repr.config(state="normal")
            else:
                na_tahu = 3 - na_tahu
                stav.set(f"Hráč {na_tahu} je na ťahu.")
            vykresli()

# funkcia na reprizu hry
def repriza():
    for b in tlacidla:
        b.config(state="disabled")
    tlacidlo_repr.config(state="disabled")
    stav.set("Prehrávam reprízu...")
    canvas.delete("all")
    vykresli(15)
    okno.after(1000, lambda: prehrat_krok(0, 15))  

def prehrat_krok(i, zostava):
    if i < len(reprizenka):
        hrac, kolko = reprizenka[i]
        nove = zostava - kolko
        vykresli(nove)
        canvas.create_text(200, 120, text=f"Hráč {hrac} zobral {kolko}", font=("Arial", 12))
        okno.after(1000, lambda: prehrat_krok(i + 1, nove))  
    else:
        canvas.create_text(200, 120, text="Koniec hry (repríza)", font=("Arial", 12))
        stav.set("Repríza dokončená.")

# tlacidla moe 
tlacidla = []
for i in range(1, 4):
    b = tkinter.Button(okno, text=f"Zobrať {i}", width=10, command=lambda i=i: tah(i))
    b.pack(side="left", padx=5, pady=5)
    tlacidla.append(b)

tlacidlo_repr = tkinter.Button(okno, text="Repríza", width=10, command=repriza, state="disabled")
tlacidlo_repr.pack(side="right", padx=5)

tkinter.Label(okno, textvariable=stav, font=("Arial", 12)).pack(pady=5)

vykresli()
okno.mainloop()
