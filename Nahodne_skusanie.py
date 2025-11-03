from random import *
pocet_studentov = int(input("Zadajte počet ziakov: "))
pocet_otazok = int(input("Zadajte počet otázok: "))
#neviem jak spravit parne a neparne otazky

ziaci = []
otazky = []
parne_cisla = []
neparne_cisla = []
pocitanie = 0

if pocet_otazok > pocet_studentov:
    print("Počet otázok musí byť menší alebo rovný počtu študentov.")
else:
    print("Poradie odpovedajúcich a ich číslo otázky: ")
    for i in range(pocet_studentov):
        ziaci.append(i + 1)
        
    for j in range(pocet_otazok):
        otazky.append(j + 1)

    for k in range(pocet_studentov):
        pocitanie += 1
        ziak = choice(ziaci)
        otazka = choice(otazky)
        ziaci.remove(ziak)
        otazky.remove(otazka)
        print(pocitanie,".",f"študent - {ziak} - otázka {otazka}")
        

        


    


