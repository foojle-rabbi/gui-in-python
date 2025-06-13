import tkinter as tk

root = tk.Tk()
root.title("RadioButton Using Loops")
root.geometry("350x400")

# define the fucntion here
def show():
    label.config(text=f"you choose: {var.get()}")

# first create the variable that will store the values
var = tk.StringVar()
var.set(None)

# jehetu eita ami manually korbo na tai amake toh options gular moddhe options dite hobe
# tai first i need to create a list of options
options = ("Python", "c++", "MySql", "Tkinter")
for i in options:
    tk.Radiobutton(root, variable=var, value=i, text=i, command=show).pack(anchor="w", pady=5)

label = tk.Label(root, text="Make your choice")
label.pack()
root.mainloop()