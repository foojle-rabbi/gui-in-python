#  I know that it can be done in various way. but as i didnt learna bout listox and option selection that is
# why am doing it with two button. 
#     1. will add 2 button to increase and decresing the size of the text
#     2. to cahnge the font style

# lets do it. it will teach you something
import tkinter as tk

# ________ define funtion here -------------
font_size = 14
def increase_size():
    global font_size
    font_size += 2
    text_widget.config(font=("Consolas", font_size))
font_size = 14
def deccrease_size():
    global font_size
    font_size -= 2
    text_widget.config(font=("Consolas", font_size))

root = tk.Tk()
root.title("Text Widget with Scrollbar")
root.geometry("400x300")

welcome_label = tk.Label(root, text="Write whatever you want: ")
welcome_label.pack()

font_size = 14
text_widget = tk.Text(root, height=10, width="30", font=("consolas", font_size))
text_widget.pack()

# now lets add 2 buttons; 1. size increase 2. size decrease
increase_button = tk.Button(root, text="+", command=increase_size)
increase_button.pack()

decrease_button = tk.Button(root, text="-", command=deccrease_size)
decrease_button.pack()

root.mainloop()