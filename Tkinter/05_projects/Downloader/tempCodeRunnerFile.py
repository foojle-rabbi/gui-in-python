# now lets make a downloader with GUI interface
import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.geometry("450x500")
root.title("Registration Form")
root.resizable(False, False)

# now lets add a label
enter_url = tk.Label(root, text="Enter the Url: ")
text_box = tk.Text(root, height=2, width=35)

# packing methods
enter_url.pack()
text_box.pack()

root.mainloop()