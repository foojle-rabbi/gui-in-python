import tkinter as tk
from tkinter import messagebox

def show_selected():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("Selection", "No item selected")
        return
    selected_items = [listbox.get(i) for i in selected_indices]
    messagebox.showinfo("Selection", "Selected items:\n" + "\n".join(selected_items))

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter an item to add")

def delete_selected():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("Delete Error", "No item selected to delete")
        return
    for i in reversed(selected_indices):  # Delete from the end to avoid index shift
        listbox.delete(i)

root = tk.Tk()
root.title("Tkinter Listbox Complete Example")
root.geometry("400x500")

# Entry for new item input
entry = tk.Entry(root)
entry.pack(pady=5)

# Add item button
add_btn = tk.Button(root, text="Add Item", command=add_item)
add_btn.pack(pady=5)

# Frame to hold listbox and scrollbar
frame = tk.Frame(root)
frame.pack()

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox with MULTIPLE selection mode and height 8
listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, height=8, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

# Insert some default items
default_items = ["Python", "C++", "Java", "JavaScript", "Go", "Rust", "Kotlin", "Swift"]
for item in default_items:
    listbox.insert(tk.END, item)

# Show selected button
show_btn = tk.Button(root, text="Show Selected Items", command=show_selected)
show_btn.pack(pady=5)

# Delete selected button
delete_btn = tk.Button(root, text="Delete Selected Items", command=delete_selected)
delete_btn.pack(pady=5)

root.mainloop()
