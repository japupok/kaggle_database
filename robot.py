import tkinter
canvas = tkinter.Canvas(width=700, height=700, bg='white')
canvas.pack()

zaciat_x, zaciat_y = 350, 350
def kreslenie():
    global zaciat_x, zaciat_y
    dlzka = int(entry1.get())
    natocenie = (entry2.get())

    x0, y0 = zaciat_x, zaciat_y
    x1, y1 = x0, y0

   

    if natocenie == "hore":
        y1 = y0 - dlzka
        print(y1)

    elif natocenie == "dole":
        y1 = y0 + dlzka
        print(y1)
       
    elif natocenie == "vlavo":
        x1 = x0 - dlzka
        print(x1)
        
    elif natocenie == "vpravo":
        x1 = x0 + dlzka
        print(x1)
        
        
    
    else:
        print('Zadal si nesprávne')
        return
    
    canvas.create_line(x0, y0, x1, y1, fill='black', width=3)
    zaciat_x, zaciat_y = x1, y1
    
   


entry1 = tkinter.Entry()
entry1.pack()

entry2 = tkinter.Entry()
entry2.pack()

button1 = tkinter.Button(text='štart', command=kreslenie)
button1.pack()

canvas.mainloop()