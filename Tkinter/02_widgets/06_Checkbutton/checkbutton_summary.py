""""
Okay checkbutton is a kind of widget jeita amara kono option check or uncheck er jonno use kori. eita simple ekta widget 
onno shob widget er moto eitar jonno o kichu steps follow kora lage. 
    1. declare a variable to store the check or uncheck value;
    2. create a checkbox tkinter.checkbutton(root, text= , variable)
    3. pack it. 

eikhane vinno jeta sheta hocche extra ekta variable delaclare kora: var = tk.intvar()

"""

import tkinter as tk

root = tk.Tk()
root.title("Checkbox in tkinter")
root.geometry("350x400")

# declare a variable for checkbutton
var = tk.IntVar()

check_button = tk.Checkbutton(root, text="I agree", variable=var)
check_button.pack()
root.mainloop()