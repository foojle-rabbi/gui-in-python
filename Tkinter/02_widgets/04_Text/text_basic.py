# #Okay fojle listen to me text is a widget like entry unlike entry its can deal with multiple lines. with this widget
# you could do a lot of things if I make a list then: 
#     1. you can get the texts from the text widget
#     2. you can get all the texts also you can control it. like start to end.
#     3. you can design the text widget coulour, font-colour, font size and font type
#     4. there also others things but lets do these firsts

import tkinter as tk
from tkinter import *
from tkinter import messagebox

# ------------------ define all the functions here

# by this funtion we can get the texts thats on the text widget
def get_texts():
    # texts = text_widget.get("1.0", "end-1c") # for text widget get function takes 2 parameters. 1 is staring index and 2 is end
    # you can also get from specific lines and char
    texts = text_widget.get("1.3", "2.5") # means start form 1st line and 3rd char to 2nd line 5 char
    print(texts)
    messagebox.showinfo("Pop up window", texts)


# also you can define a function to clear the text box
# okay lets add a function to clear the text box
def clear_text():
    text_widget.delete("1.0", END)
    # here you can control how many lines you want to clear

# the root window 
root = tk.Tk()
root.title("Text Widget")
root.geometry("350x400")

# now lets add a label first then add a text widget
welcome_label = tk.Label(root, text="Write whatever you want: ")
welcome_label.pack()

# Now add the text widget
# text_widget = tk.Text(root, height=10, width=20)
# now lets add some more feature
text_widget = tk.Text(root, height=10, width=20, font=("consolas", 14), fg="black", bg="light blue" )
# Okay I said earlier that the word are not wrapping so to do that you need to add just one thing wrap="word"
text_widget = tk.Text(root, height=10, width=20, wrap="word", font=("consolas", 14), fg="black", bg="light blue" )
text_widget.pack()

# By these line you will have create a simple text widget where you can write but there need to add more featrue
#     1. text wrapping cause text comes on half half 
#     2. font size and style
#     3. color of the background and text
#     4. get the texts from the text widget

# are are done 

# now lets add a button to get the texts
get_button = tk.Button(root, text="get text", command=get_texts, bg="green")
get_button.pack()

# this is the clear button
clear_button = tk.Button(root, text="clear text", command=clear_text, bg="red")
clear_button.pack(pady=10)

root.mainloop()