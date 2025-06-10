import tkinter as tk
from tkinter import messagebox

# define the fucntion here
def on_toggle():
    print("status: ", var.get())

# tumi chaile extra methods of use korte parba condition check kore
def on_click():
    val = var.get()
    if(val == 1):
        messagebox.showinfo("messagebox", "You checked!")
    else:
        messagebox.showerror("Warning", "You uncheked")

root = tk.Tk()
root.title("Checkbox in tkinter")
root.geometry("350x400")

# declare a variable for checkbutton
var = tk.IntVar()
# by defalut check unchecked thake but tmi chaile eita change korte parba
var.set(1)


check_button = tk.Checkbutton(root, text="I agree", variable=var, command=on_click)
check_button.pack()
root.mainloop()