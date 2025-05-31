import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("custom icon window")
root.geometry("400x500")

# set custom window icon
# root.iconbitmap("image.png") # it will throw an error bcz its only works with .ico files.

# so to work with png you need to use photimage
icon = PhotoImage(file="image.png")
root.iconphoto(True, icon)
# dont know why but not working
root.mainloop()