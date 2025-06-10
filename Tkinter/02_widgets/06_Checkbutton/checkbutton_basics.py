import tkinter as tk

root = tk.Tk()

# Define a variable to hold the state of the checkbutton
var = tk.IntVar()

# Create the checkbutton
check = tk.Checkbutton(root, text="I agree", variable=var)

# Display it
check.pack()

root.mainloop()


