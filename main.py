"""
1.	Vytvořte jednoduchou celočíselnou kalkulačku 
2.	Pro vstupy a tlačítka použijte 3 komponenty Frame s neviditelným ohraničením 
3.	Entry pro výsledek nastavte jako readonly, aby do něj uživatel nemohl zapisovat
4.	Do Entry vkládejte výsledek pomocí proměnné StringVar()
5.	Tlačítko // provádí celočíselné dělení a % provádí zbytek po dělení. Nazapomeňte na ošetření dělení nulou u těchto dvou operací!
6.	Přidejte ošetření vstupů pomocí příkazu try a zobrazení hlášky messagebox.
"""

from tkinter import *
from tkinter import messagebox

main=Tk()
main.title("Celočíselná kalkulačka")
main.geometry("350x450")


# Nadpis
heading = Label(main, text="Kalkulačka", font="Arial 24 bold")
heading.pack()


# První číslo
Frame1 = Frame(main, padx=10, pady=10)
Frame1.pack()
number1 = Label(Frame1, text="1. Číslo:")
number1.pack(side="left")
input1 = Entry(Frame1)
input1.pack(side="left")


# Druhé číslo
Frame2 = Frame(main, padx=10, pady=10)
Frame2.pack()
number2 = Label(Frame2, text="2. Číslo:")
number2.pack(side="left")
input2 = Entry(Frame2)
input2.pack(side="left")


# Funkce pro výpočty
def Plus():
    try:
        a = int(input1.get())
        b = int(input2.get())
        result = a + b
        resultVar.set(str(result))
    except:
        messagebox.showerror("Chyba","Pozor, hodnota není číslo!")
        resultVar.set("")
        input1.delete(0,END)
        input2.delete(0,END)


def Minus():
    try:
        a = int(input1.get())
        b = int(input2.get())
        result = a - b
        resultVar.set(str(result))
    except:
        messagebox.showerror("Chyba","Pozor, hodnota není číslo!")
        resultVar.set("")
        input1.delete(0,END)
        input2.delete(0,END)


def Times():
    try:
        a = int(input1.get())
        b = int(input2.get())
        result = a * b
        resultVar.set(str(result))
    except:
        messagebox.showerror("Chyba","Pozor, hodnota není číslo!")
        resultVar.set("")
        input1.delete(0,END)
        input2.delete(0,END)


def IntegerDivide():
    try:
        a = int(input1.get())
        b = int(input2.get())
        if b == 0:
            messagebox.showwarning("Výstraha","Pozor, dělení nulou není povoleno!")
            resultVar.set("")
            input2.delete(0,END)
        else:
            result = a // b
            resultVar.set(str(result))
    except:
        messagebox.showerror("Chyba","Pozor, hodnota není číslo!")
        resultVar.set("")
        input1.delete(0,END)
        input2.delete(0,END)
        

def Modulo():
    try:
        a = int(input1.get())
        b = int(input2.get())
        if b == 0:
            messagebox.showwarning("Výstraha","Pozor, dělení nulou není povoleno!")
            resultVar.set("")
            input2.delete(0,END)
        else:
            result = a % b
            resultVar.set(str(result))
    except:
        messagebox.showerror("Chyba","Pozor, hodnota není číslo!")
        resultVar.set("")
        input1.delete(0,END)
        input2.delete(0,END)


resultVar = StringVar()
resultVar.set("")


# Tlačítka početních operací
Frame3 = Frame(main, padx=10, pady=10)
Frame3.pack()
buttonPlus = Button(Frame3, text="+", width=5, command=Plus)
buttonPlus.pack(side="left")
buttonMinus = Button(Frame3, text="-", width=5, command=Minus)
buttonMinus.pack(side="left")
buttonTimes = Button(Frame3, text="*", width=5, command=Times)
buttonTimes.pack(side="left")
buttonIntegerDivide = Button(Frame3, text="//", width=5, command=IntegerDivide)
buttonIntegerDivide.pack(side="left")
buttonModulo = Button(Frame3, text="%", width=5, command=Modulo)
buttonModulo.pack(side="left")


# Výsledek
Frame4 = LabelFrame(main, text="Výsledek",  padx=10, pady=10)
Frame4.pack()
resultEntry = Entry(Frame4, state="readonly", textvariable=resultVar)
resultEntry.pack(side="left")


# Konec
end = Button(main, text="Konec", command=main.destroy, padx=10, pady=10)
end.pack()


mainloop()
