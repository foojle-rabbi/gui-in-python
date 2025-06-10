""""
Accha Fojle shono tahole monojog diya, scrollbar hocche amader ekta widget. ar eta emon ekta widget jeita onno widget 
er sathe connect kore use kora lage. like: textbox, listbox etc; so ei shob widget er sathe jodi amader scrollbar 
connect korte hoy tahole amader kichu steps follow korte hobe: 
    1. jei widget er sathe connect korba take age build korte hobe. suppose ami textbox er sathe scrollbar connect 
        korbo so age amake textbox make korte hobe. 
    then eitar jei packing eikhane amader side dite hobe right
    2. scrollbar make korte hobe. ar ei scroll bar moddhe main 3 ta parameter dite hobe 
        1. root
        2. orient = tumi ki vertically chao naki horizontally. 
        3. comman = eita kar sathe jao. kon text box er sathe chao tar name. yview.

    3. then tomake scollbar pack korte hobe; tar moddhe o tomake kichu important parameter pass korte hboe; 
        1. side 
        2. fill y
    4. eibar text box er sathe scrollbar connect korar jonno text_box.configure( ycommanview = scrolbar_name.set)

Baach toamr kaj shesh tumi ei koyekta steps follow korlei ekta texbox er sathe ekta scrollbar connect korte parba. 
yes its true that there are a lots of configuration you can do with these. but basically you can connect and use the 
scrolllbar with the text_box by following these 4 steps. 


"""

import tkinter as tk

root = tk.Tk()

text_box = tk.Text(root)
text_box.pack(side="left")

# text box er moddhe kichu line rakhi
for i in range(101):
    text_box.insert("end", f"hello world {i}\n")

# now make a scrollbar 
scroll_bar = tk.Scrollbar(root, orient="vertical", command=text_box.yview)
scroll_bar.pack(side="right", fill="y")

text_box.configure(yscrollcommand=scroll_bar.set)

# yes now your scrollbar has connected with your text_box widget

root.mainloop()