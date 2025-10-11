import tkinter
canvas = tkinter.Canvas(width=1000, height=1000, bg='white')
canvas.pack()

with open("x.txt", "r", encoding="utf-8") as subor:
    x = [int(i) for i in subor.read().split()]

with open("y.txt", "r", encoding="utf-8") as subor:
    y = [int(i) for i in subor.read().split()]
    

r = 3

for i in range(len(x)):
    canvas.create_oval(x[i]-r, y[i]-r, x[i]+r, y[i]+r, fill="black", outline="black")
    canvas.update()
    canvas.after(50)



canvas.mainloop()