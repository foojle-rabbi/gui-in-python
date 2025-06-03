from tkinter import *

root = Tk()

text_widget = Text(root, height=10, width=40)
text_widget.pack()

root.mainloop()

# --------------------- with get, and delte 

from tkinter import *

def show_text():
    content = text.get("1.0", "end-1c")
    print("Text content:", content)

def clear_text():
    text.delete("1.0", END)

root = Tk()
text = Text(root, height=5, width=30)
text.pack()

Button(root, text="Show Text", command=show_text).pack()
Button(root, text="Clear Text", command=clear_text).pack()

root.mainloop()

