import tkinter
from random import *
canvas = tkinter.Canvas(width=800, height=200)
canvas.pack()
pismena = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
tanier = [0]*10
viacnasobne = []
puknuty_tanier = randrange(10)
def taniere():
    y = 100
    for i in range(10):
        x = 40 + i*80
        canvas.create_oval(x-30, y-30, x+30, y+30, fill='blue', width=2)
        canvas.create_text(x, y, text=pismena[i], font=('Arial', 20), fill='white')

def klik(sur):
    global tanier
    x = sur.x
    y = sur.y
    
    for i in range(10):
        cx = 40 + i*80
        cy = 100
        if abs(x - cx) <= 30 and abs(y - cy) <= 30:
            tanier[i] += 1
            klik_tanier = pismena[i], tanier[i]
            print(klik_tanier)

            if i == puknuty_tanier:
                
                canvas.create_line(cx-20, cy-20, cx+20, cy+20, fill='black', width=4)
                canvas.create_line(cx+20, cy-20, cx-20, cy+20, fill='black', width=2)
                canvas.delete('all')
                canvas.create_text(400, 30, text='Gratulujem, označil si puknutý tanier!', font=('Arial', 20), fill='red')
                 
                
                for j in range(10):
                    if tanier[j] > 1:
                        viacnasobne.append(pismena[j])

                
                if viacnasobne:
                    canvas.create_text(400, 100, text=f"Viackrát si klikol na taniere: {viacnasobne}", font=('Arial', 16), fill='red')
                else:
                    canvas.create_text(400, 100, text="Na žiadny tanier si neklikol viackrát.", font=('Arial', 16), fill='red')

                #staci return ale moze tam byt aj unbind
                canvas.unbind('<Button-1>')
                return
                
                
            
taniere()
canvas.bind('<Button-1>',klik)
canvas.mainloop()
