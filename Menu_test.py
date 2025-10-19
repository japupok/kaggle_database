import tkinter as tk
from tkinter import ttk

# ===== Funkcie pre jednotlivé okná =====

def otvor_checkbutton():
    okno = tk.Toplevel(root)
    okno.title("Checkbutton – viacnásobný výber")

    popis = tk.Label(okno, text="Checkbutton")
    popis.pack(pady=5)

    var1, var2, var3 = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()

    def zobraz():
        vybrane = []
        if var1.get(): vybrane.append("Hudba")
        if var2.get(): vybrane.append("Šport")
        if var3.get(): vybrane.append("Cestovanie")
        text = ", ".join(vybrane) if vybrane else "nič"
        vysledok.config(text=f"Zaujíma ťa: {text}")

    c1 = tk.Checkbutton(okno, text="Hudba", variable=var1, command=zobraz)
    c2 = tk.Checkbutton(okno, text="Šport", variable=var2, command=zobraz)
    c3 = tk.Checkbutton(okno, text="Cestovanie", variable=var3, command=zobraz)
    c1.pack(anchor="w"); c2.pack(anchor="w"); c3.pack(anchor="w")

    vysledok = tk.Label(okno, text="Zatiaľ nič neoznačené")
    vysledok.pack(pady=5)


def otvor_scale():
    okno = tk.Toplevel(root)
    okno.title("Scale – posuvník")

    popis = tk.Label(okno, text="Scale.")
    popis.pack(pady=5)

    def zmena(val):
        vysledok.config(text=f"Hodnota: {int(float(val))}")

    s = tk.Scale(okno, from_=0, to=100, orient="horizontal", command=zmena)
    s.pack(padx=10, pady=5)
    vysledok = tk.Label(okno, text="Hodnota: 0")
    vysledok.pack()


def otvor_spinbox():
    okno = tk.Toplevel(root)
    okno.title("Spinbox – číselný vstup")

    popis = tk.Label(okno, text="Spinbox.")
    popis.pack(pady=5)

    def zobraz():
        vysledok.config(text=f"Zadané číslo: {spin.get()}")

    spin = tk.Spinbox(okno, from_=1, to=10, width=5, command=zobraz)
    spin.pack(pady=5)

    vysledok = tk.Label(okno, text="Zadané číslo: 1")
    vysledok.pack()


def otvor_listbox():
    okno = tk.Toplevel(root)
    okno.title("Listbox – výber zo zoznamu")

    popis = tk.Label(okno, text="Listbox.")
    popis.pack(pady=5)

    lb = tk.Listbox(okno)
    for farba in ["Červená", "Zelená", "Modrá", "Žltá", "Fialová"]:
        lb.insert(tk.END, farba)
    lb.pack(pady=5)

    def zobraz(event):
        vybr = lb.get(lb.curselection())
        vysledok.config(text=f"Vybral si: {vybr}")

    lb.bind("<<ListboxSelect>>", zobraz)
    vysledok = tk.Label(okno, text="Zatiaľ nevybrané")
    vysledok.pack()


def otvor_combobox():
    okno = tk.Toplevel(root)
    okno.title("Combobox – rozbaľovacie menu")

    popis = tk.Label(okno, text="Combobox.")
    popis.pack(pady=5)

    def zobraz(event):
        vysledok.config(text=f"Zvolil si: {combo.get()}")

    combo = ttk.Combobox(okno, values=["Január", "Február", "Marec", "Apríl"])
    combo.current(0)
    combo.bind("<<ComboboxSelected>>", zobraz)
    combo.pack(pady=5)

    vysledok = tk.Label(okno, text="Zvolil si: Január")
    vysledok.pack()


# ===== Hlavné okno =====
root = tk.Tk()
root.title("Tkinter")

# Hlavné menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

dizajn_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Dizajn", menu=dizajn_menu)
dizajn_menu.add_command(label="Checkbutton", command=otvor_checkbutton)
dizajn_menu.add_command(label="Scale", command=otvor_scale)
dizajn_menu.add_command(label="Spinbox", command=otvor_spinbox)
dizajn_menu.add_command(label="Listbox", command=otvor_listbox)
dizajn_menu.add_command(label="Combobox", command=otvor_combobox)

# ===== Widget priamo v hlavnom okne =====
uvod = tk.Label(root, text="Ukážka widgetu Radiobutton (hlavné okno)")
uvod.pack(pady=10)

v = tk.StringVar(value="")

def zobraz():
    vysledok.config(text=f"Vybral si: {v.get()}")

r1 = tk.Radiobutton(root, text="Červená", variable=v, value="Červená", command=zobraz)
r2 = tk.Radiobutton(root, text="Zelená", variable=v, value="Zelená", command=zobraz)
r3 = tk.Radiobutton(root, text="Modrá", variable=v, value="Modrá", command=zobraz)
r1.pack(anchor="w"); r2.pack(anchor="w"); r3.pack(anchor="w")

vysledok = tk.Label(root, text="Zatiaľ nevybrané")
vysledok.pack(pady=10)



root.mainloop()
