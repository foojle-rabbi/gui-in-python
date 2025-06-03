import tkinter as tk

# Initial sizes
font_size = 14
text_height = 10
text_width = 30

def update_text_widget():
    text_widget.config(font=("Consolas", font_size), height=text_height, width=text_width)

def increase_size():
    global font_size
    font_size += 1
    update_text_widget()

def decrease_size():
    global font_size
    if font_size > 1:
        font_size -= 1
        update_text_widget()

def increase_height():
    global text_height
    text_height += 1
    update_text_widget()

def decrease_height():
    global text_height
    if text_height > 1:
        text_height -= 1
        update_text_widget()

def increase_width():
    global text_width
    text_width += 1
    update_text_widget()

def decrease_width():
    global text_width
    if text_width > 1:
        text_width -= 1
        update_text_widget()

root = tk.Tk()
root.title("Resizable Text Widget")
root.geometry("500x400")

tk.Label(root, text="Write whatever you want:").pack()

text_widget = tk.Text(root, font=("Consolas", font_size), height=text_height, width=text_width)
text_widget.pack()
text_widget.pack_propagate(False)

# --- Font size buttons ---
font_frame = tk.Frame(root)
font_frame.pack(pady=5)

tk.Label(font_frame, text="Font:").pack(side="left")
tk.Button(font_frame, text="+", command=increase_size).pack(side="left", padx=2)
tk.Button(font_frame, text="-", command=decrease_size).pack(side="left", padx=2)

# --- Height buttons ---
height_frame = tk.Frame(root)
height_frame.pack(pady=5)

tk.Label(height_frame, text="Height:").pack(side="left")
tk.Button(height_frame, text="+", command=increase_height).pack(side="left", padx=2)
tk.Button(height_frame, text="-", command=decrease_height).pack(side="left", padx=2)

# --- Width buttons ---
width_frame = tk.Frame(root)
width_frame.pack(pady=5)

tk.Label(width_frame, text="Width:").pack(side="left")
tk.Button(width_frame, text="+", command=increase_width).pack(side="left", padx=2)
tk.Button(width_frame, text="-", command=decrease_width).pack(side="left", padx=2)

root.mainloop()
