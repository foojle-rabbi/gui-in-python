import tkinter as tk

def show_selection():
    print("Python:", python_var.get())
    print("Java:", java_var.get())

root = tk.Tk()

python_var = tk.IntVar()
java_var = tk.IntVar()

cb1 = tk.Checkbutton(root, text="Python", variable=python_var)
cb2 = tk.Checkbutton(root, text="Java", variable=java_var)
btn = tk.Button(root, text="Check", command=show_selection)

cb1.pack()
cb2.pack()
btn.pack()

root.mainloop()
