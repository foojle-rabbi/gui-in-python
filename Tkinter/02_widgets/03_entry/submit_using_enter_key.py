# Here we can simply use the enter key to submit something
import tkinter as tk
from tkinter import messagebox

# define the function here ----------------
def sub_btn_click(event = None): # so error handle koar jonno we need to set a arguments
    # lets implement our logic here when our submit button is clicked
    # Accha eikhane temon beshi kichu korbo na. just
    name = input_name.get()

    if name:
        messagebox.showinfo("Submitted successfully", f"Jajakallah: {name}")
        clear_input()
    else:
        messagebox.showwarning("Warning message", "please fill the box")

def clear_input():
    input_name.delete(0, tk.END)

# root window 
root = tk.Tk()
root.geometry("350x400")
root.title("Exploring Entry Widget")

# labels inputs and buttons
input_name = tk.Entry(root, width=20)
input_name.pack()

# now lets add a buton
submit_button = tk.Button(root, text="Submit", bg="light blue", command=sub_btn_click)
submit_button.pack(pady=10)
# Okay the code we have written was simple and easirer. but now we want to submit the info using enter key so,
# for that we need to use
root.bind('<Return>', sub_btn_click) # Okay if i press enter then it will throw an error. because every key takes an 
# arguemnt

root.mainloop()