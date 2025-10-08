#Create a simple integer calculator.
#Use 3 Frame components with an invisible border for the inputs and buttons.
#Set the result Entry to readonly, so the user cannot write into it.
#Insert the result into the Entry using a StringVar() variable.
#The // button performs integer division and the % button performs the remainder of the division (modulo). Don't forget to handle division by zero for these two operations!
#Add input handling using a try-except block and display a messagebox on error.


from tkinter import *
from tkinter import messagebox

# Main window setup
root = Tk()
root.title("Integer Calculator")
root.geometry("350x450")

# Heading
heading_label = Label(root, text="Calculator", font="Arial 24 bold")
heading_label.pack()

# --- First Number Input ---
frame_num1 = Frame(root, padx=10, pady=10)
frame_num1.pack()
label_num1 = Label(frame_num1, text="1st Number:")
label_num1.pack(side="left")
entry_num1 = Entry(frame_num1)
entry_num1.pack(side="left")

# --- Second Number Input ---
frame_num2 = Frame(root, padx=10, pady=10)
frame_num2.pack()
label_num2 = Label(frame_num2, text="2nd Number:")
label_num2.pack(side="left")
entry_num2 = Entry(frame_num2)
entry_num2.pack(side="left")

# --- Calculation Functions ---
def add():
    try:
        a = int(entry_num1.get())
        b = int(entry_num2.get())
        result = a + b
        result_var.set(str(result))
    except ValueError:
        messagebox.showerror("Error", "Attention, the value is not a number!")
        result_var.set("")
        entry_num1.delete(0, END)
        entry_num2.delete(0, END)

def subtract():
    try:
        a = int(entry_num1.get())
        b = int(entry_num2.get())
        result = a - b
        result_var.set(str(result))
    except ValueError:
        messagebox.showerror("Error", "Attention, the value is not a number!")
        result_var.set("")
        entry_num1.delete(0, END)
        entry_num2.delete(0, END)

def multiply():
    try:
        a = int(entry_num1.get())
        b = int(entry_num2.get())
        result = a * b
        result_var.set(str(result))
    except ValueError:
        messagebox.showerror("Error", "Attention, the value is not a number!")
        result_var.set("")
        entry_num1.delete(0, END)
        entry_num2.delete(0, END)

def integer_divide():
    try:
        a = int(entry_num1.get())
        b = int(entry_num2.get())
        if b == 0:
            messagebox.showwarning("Warning", "Attention, division by zero is not allowed!")
            result_var.set("")
            entry_num2.delete(0, END)
        else:
            result = a // b
            result_var.set(str(result))
    except ValueError:
        messagebox.showerror("Error", "Attention, the value is not a number!")
        result_var.set("")
        entry_num1.delete(0, END)
        entry_num2.delete(0, END)

def modulo():
    try:
        a = int(entry_num1.get())
        b = int(entry_num2.get())
        if b == 0:
            messagebox.showwarning("Warning", "Attention, division by zero is not allowed!")
            result_var.set("")
            entry_num2.delete(0, END)
        else:
            result = a % b
            result_var.set(str(result))
    except ValueError:
        messagebox.showerror("Error", "Attention, the value is not a number!")
        result_var.set("")
        entry_num1.delete(0, END)
        entry_num2.delete(0, END)

# Variable to hold the result
result_var = StringVar()
result_var.set("")

# --- Operation Buttons ---
operations_frame = Frame(root, padx=10, pady=10)
operations_frame.pack()

button_add = Button(operations_frame, text="+", width=5, command=add)
button_add.pack(side="left")
button_subtract = Button(operations_frame, text="-", width=5, command=subtract)
button_subtract.pack(side="left")
button_multiply = Button(operations_frame, text="*", width=5, command=multiply)
button_multiply.pack(side="left")
button_integer_divide = Button(operations_frame, text="//", width=5, command=integer_divide)
button_integer_divide.pack(side="left")
button_modulo = Button(operations_frame, text="%", width=5, command=modulo)
button_modulo.pack(side="left")

# --- Result Display ---
result_frame = LabelFrame(root, text="Result", padx=10, pady=10)
result_frame.pack()
result_entry = Entry(result_frame, state="readonly", textvariable=result_var)
result_entry.pack(side="left")

# --- Exit Button ---
exit_button = Button(root, text="Exit", command=root.destroy, padx=10, pady=10)
exit_button.pack()

# Start the main event loop
root.mainloop()
