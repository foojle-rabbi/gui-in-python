from tkinter import *

def show_selection():
    selected = var.get()
    label.config(text=f"You selected Option {selected}")

root = Tk()
root.title("RadioButton Example")
root.geometry("350x400")

var = IntVar()

Radiobutton(root, text="Option 1", variable=var, value=1, command=show_selection).pack()
Radiobutton(root, text="Option 2", variable=var, value=2, command=show_selection).pack()
Radiobutton(root, text="Option 3", variable=var, value=3, command=show_selection).pack()

label = Label(root, text="Make a selection")
label.pack()

root.mainloop()
