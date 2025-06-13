"""
Scale holo khub important ekta widget jeita amader onek kajei lagbe; Jemon volume simulator, zoom in, zoom out, brightness 
control etc; Toh cholo eibar eitare khub easy bashay simple bashay buijha nei je kivabe kaj kore

toh eitar jonno o kichu steps ache. kichu extra features o ache; Lets see the steps
    1. first create a variable
    2. then tk.scale() tar moddhe koyekta important parameter pass korte hobe sheigula holo:
        a. from_= orthat koto theke scale ta shuru hobe
        b. to= koto porjono lagbe
        c. orient= tk.VERTICAl or Horizontal
        d. length= eita dekhte koto boro hobe la lombay koto tuku hobe
        e. resulation= each time koto kore barbe ba kombe
        f. tickinterval= scale e koto por por show korbe. like title er moto
        g. label= scale er text ba label
        h. command= scale click korle ki hobe
    3. tumi chaile eitar value initially koto hobe sheitao set kore dite paro using set() method
"""

# now lets make a basic scale using these things
import tkinter as tk
from tkinter import messagebox

# our methods will be here
def show_info(val):
    # var = scale_bar.get()
    # i think scale er value automatic parameter hisebe aisha pore
    # amader kache val ta ashe hocche string akare tai take age integer e convert korte hobe 
    val = int(val)
    label.config(text=f"Your scale is now on : {val}%")

    # now lets show a warning if it goes higher than 75%
    if(val > 75):
        messagebox.showwarning("Warning", "Volume is High")
# arrow key confirmations
def on_left_click(event):
    # print("Pressed <--")
    val = int(scale_bar.get())
    scale_bar.set(val-5)

# now lets bind with the scale widget 
def on_right_click(event):
    # print("Pressed -->")
    val = int(scale_bar.get())
    scale_bar.set(val+5)
    # Yes finally it succesed

root = tk.Tk()
root.title("Scale Widget summary")
root.geometry("400x200")
root.resizable(False, False)

# Eikhane amader sacle er varialbe create kora hobe
scale_bar = tk.Scale(root, from_=0, to=100, label="This is a test scale", length=300, 
                     resolution=5, tickinterval=25, orient=tk.HORIZONTAL, command=show_info)
scale_bar.pack()
scale_bar.set(50)

# lets add a label to ge the idea
label = tk.Label(root, text="Your scale is now on : 50%")
label.pack()

# lets try to bind arrow keys
root.bind("<Right>", on_right_click)
root.bind("<Left>", on_left_click)
# Now lets also bind the up and down keys also
root.bind("<Up>", on_right_click)
root.bind("<Down>", on_left_click)

root.mainloop()