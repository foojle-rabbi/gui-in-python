# accha ekhon amra janbo kivabe submit button er help niye kono kichu captuare kore. like jodi name enter kore submit kore
# tahole amra oi name kivabe capture korte parbo. tar jonno amader ke submit button er moddhe ekta special parameter command 
# pass korte hobe. ar comman er moddhe amader ekta fucntion thakte hobe. mane command mane button e click korel ki hobe?
# kono function run hobe? tahole kon function run hobe? ebong function er moddhe ki ki kaj hobe?
import tkinter

# Eikhanei amader function define korte hobe jeikhane submit e click/comman korle kon function trigger hobe
def onClick():
    print("Submit button clicked")
    # name = name_textbox # ashole eivabe dile kaj hobe na. jodi texbox theke value dorkar hoy tahole .get() use
    name = name_textbox.get()
    if name:
        print(name)
    else:
        print("You enterd nothing.")
    


root = tkinter.Tk()
root.geometry("350x400")
root.title("My App")

name_label = tkinter.Label(root, text="Enter your name")
name_label.pack()

name_textbox = tkinter.Entry(root)
name_textbox.pack()

# now lets add submit button
submit_button = tkinter.Button(root, text="Submit", command=onClick)
submit_button.pack()
root.mainloop()