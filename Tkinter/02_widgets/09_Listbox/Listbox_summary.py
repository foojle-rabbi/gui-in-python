"""
Accha List box widget somporke temon beshi kichu bujhlam na. just eituku e bujhlam je eitar maddhome option select kora
jay insert kora. single select kora jay multiple select kora jay. eita onekta dropdown menu er moto hoileo eita 
drop down menu na. 

Toh cholo dekhi eita asole kivabe kaj kore 
"""

import tkinter as tk

root = tk.Tk()
root.title("List Box sumamry")
root.geometry("400x500")

# our functions will be defined here
def insert_iteam(event): # enter key binding korle event set kora lage
    iteam = optn_entry.get()
    list_box.insert(tk.END, iteam)
    # optn_entry.delete(tk.END, 0) # syntax ulta lekhi
    optn_entry.delete(0, tk.END) # syntax ulta lekhi

# lets see what comes 
list_box = tk.Listbox(root)
list_box.pack()

# now lests insert some options
list_box.insert("end", "Dhaka")
list_box.insert("end", "Cumilla")
list_box.insert("end", "Rajshahi")
list_box.insert("end", "Khulna")

# cholo eibar loop er maddhome insert kore dekhi 
fruits = ("Apple", "Banana", "Black berry", "Mango")

for i in fruits:
    list_box.insert(tk.END, i)

# accha uporer code gula ki korche sheita bujhechi. ekta empty list box create korche then kichu iteams push korche.

# toh age entry or text dorkar
optn_entry = tk.Entry(root)
optn_entry.pack()

# ekhon ami chaile amar nijer insert function / button create korte pari. dekhba?
insert_btn = tk.Button(root, text="insert", command=insert_iteam(None))
insert_btn.pack()

# hah ha but ki insert korba? insert er jnno to entry ba text dorkar tai nai?? tai age enty or text dorakr


# lets bind the enter key also
root.bind("<Return>", insert_iteam)

# lets add a scroll widget for list box
scroll_bar = tk.Scrollbar(root, orient=tk.VERTICAL, command=list_box.yview)
scroll_bar.pack(side="right", fill="y")
list_box.configure(yscrollcommand=scroll_bar.set)

"""
Accha taile eituku toh bujhlam je kemne listbox create korte hoy. kivabe manually insert korte hoy kivabe loop diye insert korte
hoy. kivabe gui er maddhome entry/textbox use kore insert korte hoy. eitoh arki? 

okay arekta kaj ache cholo ei list box er iteams er moddhe ekta scrollbar add kori. Accha scroll bar ta Frame dia tray kori
arekta file e. But before that I think I should about "Frame"
"""
root.mainloop()