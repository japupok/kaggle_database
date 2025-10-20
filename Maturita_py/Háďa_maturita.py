import tkinter
canvas = tkinter.Canvas(width=800,height=800)
canvas.pack()

def posun():
    global xhlava,yhlava,narazenie
    xhlava += sx
    yhlava += sy
    z = canvas.coords('hada')
    zx = z[::2]
    zy = z[1::2]
    i = 0
    while i < len(zx) and not narazenie:
        if zx[i] == xhlava and zy[i] == yhlava:
            narazenie = True
        i += 1

    if not narazenie:
        z.append(xhlava)
        z.append(yhlava)
        canvas.coords('hada',z)
        canvas.after(10,posun)
    
def klaves(event):
    global sx,sy
    if event.keysym == 'Left':
        sx,sy = -1, 0
    if event.keysym == 'Right':
        sx,sy = 1,0
    if event.keysym == 'Up':
        sx,sy = 0,-1
    if event.keysym == 'Down':
        sx,sy = 0,1
    
narazenie = False
xhlava, yhlava = 200,200
sx,sy = 0, -1
canvas.create_line(xhlava,yhlava-sy,xhlava,yhlava,tags='hada')
posun()
canvas.bind_all('<Key>',klaves)



canvas.mainloop()