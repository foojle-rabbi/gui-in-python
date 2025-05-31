import tkinter as tk

root = tk.Tk()

root.geometry("350x400")

root.title("resizeable Property")

# Accha eita hocche ekta normal window create korar code. so geometry("") use kroar karon amader defaut e 
# ei size e open hobe. pore amra chaile boro choto korte parbo. but jodi resizeable() property use kori tahole

# root.resizable(True, True) # means height and width resizeable
root.resizable(True, False) # means only width resiazeable
# root.resizable(False, True) # height resiable
# root.resizable(False, False) # you cant change the height and width
root.mainloop()