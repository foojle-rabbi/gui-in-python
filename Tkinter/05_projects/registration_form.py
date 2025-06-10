# lets make a registration box with checkbox and submit button
    # Here I will include
    # 1. Name
    # 2. Phone number
    # 3. Email Address
    # 4. Password
    # 5. I agree with the terms and conditions
    # 6. Submit button

# insha-allah in future I will connect with the google sheets or ms excel

# -------------------------- 
import tkinter as tk
from tkinter import messagebox

# define the fucntion here
# lefts first define a function that will show error
def show_error(msg):
    messagebox.showwarning("Showing Warning", msg)

def on_click(event = None):
    # messagebox.showinfo("Message", "Submittet Successfully")
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    pass_word = password_entry.get()

    if(name and email and phone):
        # now check by one by one
        # check the name first
        if(name.isdigit()):
            show_error("Enter a valid name")
        
        # first check if the email is valid or not
        if(not email.endswith("@gmail.com")):
            show_error("Invalid Email")
        
        # now check the phone number validity
        if(not phone.isdigit() or len(phone) != 11 or not phone.startswith(('0', '1'))):
            show_error("Invalid Phone")
        
        # now check the phone pass word
        # if evertyings fine then show a message
        messagebox.showinfo("Submitted Succesfully", "Submitted Succesfully")
    else:
        messagebox.showerror("Error message", "Fill up the boxes")


# root window
root = tk.Tk()
root.geometry("450x500")
root.title("Registration Form")
root.resizable(False, False)


# entrys
check_var = tk.IntVar()

# Informatoin
name = tk.Label(root, text="Enter your Name: ", font=("Arial", 15))
name_entry = tk.Entry(root, width=25)
email = tk.Label(root, text="Enter your Email: ", font=("Arial", 15))
email_entry = tk.Entry(root, width=25)
phone = tk.Label(root, text="Enter your Phone: ", font=("Arial", 15))
phone_entry = tk.Entry(root, width=25)
password = tk.Label(root, text="Enter your Password: ", font=("Arial", 15))
password_entry = tk.Entry(root, width=25)
conf_pass = tk.Label(root, text="Confirm Your Password: ", font=("Arial", 15))
conf_pass_entry = tk.Entry(root, width=25)

# submit button and checkbutton
check_btn = tk.Checkbutton(root, text="I agree with the terms and condition")
submit_btn = tk.Button(root, text="Register", command=on_click)

# pack them
name.pack()
name_entry.pack()
email.pack()
email_entry.pack()
phone.pack()
phone_entry.pack()
password.pack()
password_entry.pack()
conf_pass.pack()
conf_pass_entry.pack()

# button adn checkbtton
check_btn.pack()
submit_btn.pack(ipadx=10)

# Take intput from keyboard (enter key)
root.bind('<Return>', on_click)
root.mainloop()