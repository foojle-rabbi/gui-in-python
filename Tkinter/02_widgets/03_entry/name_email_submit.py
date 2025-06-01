# Okay then lets create a window where there will be name email input and a submit button
import tkinter as tk
from tkinter import messagebox

# ---------------- will define the functions here --------------------------
def btn_click():
    # button click kora hoile input box er information gula neo
    name = name_input.get()
    email = email_input.get()

    # wait wait tumi chaile kintu error dekhaite paro jodi name othoba email feild khali thake
    if name and email:
        # wah keya baat hain keya baat hain i can check condition here its great
        if (name.isdigit()) or ("@gmail.com" not in email):
            messagebox.showerror("Warning!", "Invalid input")
        else:
            messagebox.showinfo("Submitted successfully", f"your name: {name}\nEmail: {email}")
            clear_input()   
    # ami toh chaile eikhane aro condition use korte pari like
    else:
        messagebox.showwarning("Warning!", "Please fill the inputbox")


    # inofrmation gula eibar msg box othoba pop ups er maddhomeo show korte paro
    # messagebox.showinfo()


def clear_input():
    name_input.delete(0, tk.END)
    email_input.delete(0, tk.END)


# ---------------- main window -------------------
root = tk.Tk()
root.geometry("350x400")
root.title("Exploring Entry Widget")
root.configure(bg="grey")

# -------------- here will be the lable, input box and buttons ----------------
name_label = tk.Label(root, text="Enter your name: ", font=("roboto", 16), fg="yellow", bg="black")
name_label.pack(pady=5)

name_input = tk.Entry(root, width=20)
name_input.pack()

email_label = tk.Label(root, text="Enter your email: ", font=("roboto", 16), fg="yellow", bg="black")
email_label.pack(pady=2)

email_input = tk.Entry(root, width=20)
email_input.pack(pady=2)

submit_button = tk.Button(root, text="Submit", bg="lightgreen", command=btn_click)
submit_button.pack()

root.mainloop()