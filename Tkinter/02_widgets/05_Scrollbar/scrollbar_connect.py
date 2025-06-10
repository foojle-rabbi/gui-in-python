import tkinter as tk

root = tk.Tk()
root.geometry("350x400")
root.title("Scrollbar Connect")

text_box = tk.Text(root)

for i in range(50):
    text_box.insert("end", f"Hello world {i}\n")
text_box.pack(side="left")

# uporer code gula dia ekta text box banaichi jar moddhe 50 tar moto line ache. amra chaile eigular moddhe
# mouse diye ba arrow key diye scroll korte pari. but eitar moddhe inbuild scrollbar nai. sheitar jonno amader
# ke alada kore scrollbar add korte hobe. tar jonno ekta scrollbar widget make korte hobe make korar por tar moddhe
# 2 ta paramter dite hobe orientation and command; 
scroll_bar = tk.Scrollbar(root, orient="vertical", command=text_box.yview)
# shudhu eituku korlei hobe na tar por ei scroll bar ke texbox widget er sathe connec korte hobe. 
text_box.configure(yscrollcommand=scroll_bar.set)
# scroll_bar.pack() # ekhon shudhu pack korlei hobe na. kon side e chao sheita o lagbe
scroll_bar.pack(side="right", fill="y")

root.mainloop()