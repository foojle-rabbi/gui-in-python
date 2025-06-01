# Okay then lets try exploring the entry widget 

import tkinter as tk

# ------------ lets create aout functions here
def sub_btn_click():
    name = input_name.get() # ei get method use kroe amra input_name field theke dta nibo
    print(name)
    # cholo submit button click korar por name print hoyar por e input feild means name feild clear kore feli
    clear_entry()
    print("Clear function called and cleard the name entry")

# now lets define a celar function to clear the input feilds 
def clear_entry():
    input_name.delete(0, tk.END) # eita amader name input theke data delte korbe

root = tk.Tk()
root.geometry("350x400")
root.title("Exploring Entry Widget")

# okay lets add some label
welcome_text = tk.Label(root, text="Welcome to my App", font=("Arial", 15))
welcome_text.pack(pady=20)

# now lets add a input box 
input_name = tk.Entry(root, width=20)
input_name.pack()

# Okay then amra tahole ekta welcome text create korlam then ekta input feild create korlam. 
# jodio ei entry box niye onek kichu e kora jay. means amar kache onek option ache to customize

# now lets add a buton
submit_button = tk.Button(root, text="Submit", command=sub_btn_click)
submit_button.pack(pady=10)

root.mainloop()