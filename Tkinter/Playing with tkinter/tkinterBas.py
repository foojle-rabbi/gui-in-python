import tkinter

root = tkinter.Tk()

root.geometry("350x400")
root.title("My first App")

#now lets create a lebel. Tumi lebel re text hisebeo dhorte paro.
name_label = tkinter.Label(root, text="Enter your name")
name_label.pack()

# amra textbox anar jonno entry use kori. ar tar moddhe parameter dei kothay crate korte chai. 
name_textbox = tkinter.Entry(root)
name_textbox.pack() # ar pack chara amader ei variable window te show korbe na. 

# now lets create a submit button
submit_button = tkinter.Button(root, text="Submit")
submit_button.pack() # but eita use korle tomar button ashbe but oitar moddhe kichu lekha aste na. tar jonno upore 

root.mainloop()