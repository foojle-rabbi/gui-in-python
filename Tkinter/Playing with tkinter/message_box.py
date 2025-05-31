import tkinter
from tkinter import messagebox # message box show korar jonno
root = tkinter.Tk()

# Amader ei jei function ta eikhane terminal e masg gula show kore but amra chacchi window te mas aakare show korte tahole
# def onClick():
#     print("Submit button clicked")
#     name = name_textbox.get()
#     if name:
#         print(name)
#     else:
#         print("You enterd nothing.")
    
def onClick():
    name = name_textbox.get()
    messagebox.showinfo("Captuared Data", "Successful")

root.geometry("350x400")
root.title("My App")

name_label = tkinter.Label(root, text="Enter your name")
name_label.pack()

name_textbox = tkinter.Entry(root)
name_textbox.pack()

# now lets add submit button
submit_button = tkinter.Button(root, text="Submit", command=onClick)
submit_button.pack()
root.mainloop()