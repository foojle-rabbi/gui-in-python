import tkinter as tk

root = tk.Tk()
root.title("Scale widget Practice")
root.geometry("350x400")

# lets make a horizontal scale 0 to 100
hor_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="A scle", resolution=10, length=300, tickinterval=50)
hor_scale.pack()

root.mainloop()