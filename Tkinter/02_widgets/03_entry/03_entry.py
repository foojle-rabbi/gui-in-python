import tkinter as tk
from tkinter import messagebox

# --- Create main window ---
root = tk.Tk()
root.title("Entry Widget Full Example")
root.geometry("400x300")
root.configure(bg="white")

# --- Instruction Label ---
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

# --- Entry Field (Normal Entry) ---
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.insert(0, "Type here...")  # Pre-fill text
entry.pack(pady=5)

# --- Password Entry Field ---
label_pass = tk.Label(root, text="Enter your password:", font=("Arial", 12))
label_pass.pack(pady=10)

password_entry = tk.Entry(root, width=30, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

# --- Function to Show Entry Data ---
def show_text():
    name = entry.get()
    password = password_entry.get()

    # If entry is disabled, it can't be fetched
    messagebox.showinfo("Entered Data", f"Name: {name}\nPassword: {password}")
    print("Name:", name)
    print("Password:", password)

# --- Function to clear entries ---
def clear_entries():
    entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# --- Disable/Enable Entry Example ---
def disable_entry():
    entry.configure(state="disabled")
    password_entry.configure(state="disabled")

def enable_entry():
    entry.configure(state="normal")
    password_entry.configure(state="normal")

# --- Submit Button ---
submit_btn = tk.Button(root, text="Submit", command=show_text, bg="lightblue", font=("Arial", 10))
submit_btn.pack(pady=10)

# --- Clear Button ---
clear_btn = tk.Button(root, text="Clear", command=clear_entries, bg="lightyellow", font=("Arial", 10))
clear_btn.pack(pady=5)

# --- Disable & Enable Buttons ---
disable_btn = tk.Button(root, text="Disable Inputs", command=disable_entry, bg="tomato", font=("Arial", 10))
disable_btn.pack(pady=5)

enable_btn = tk.Button(root, text="Enable Inputs", command=enable_entry, bg="lightgreen", font=("Arial", 10))
enable_btn.pack(pady=5)

# --- Start mainloop ---
root.mainloop()
