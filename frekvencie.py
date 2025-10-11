import tkinter
from random import *
canvas = tkinter.Canvas(width=650, height=600, bg='white')
canvas.pack()

freq = (31, 62, 125, 250, 500, "1K", "2K", "4K", "8K", "16K")
def eq():
    canvas.delete('all')
    for i in range(10):
        vyska = randint(0, 450)
        canvas.create_rectangle(60*i+5, 500, 60*(i+1), 500-vyska, fill='green')
        canvas.create_text(60*i+30, 520, text=freq[i])
        canvas.create_text(60*i+30, 480-vyska, text=str(vyska))
    canvas.create_text(625, 520, text="[Hz]")
       
        
        
   
    canvas.update()
    canvas.after(350,eq)



eq()
canvas.mainloop()