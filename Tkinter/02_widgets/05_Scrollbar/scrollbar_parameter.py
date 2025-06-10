import tkinter as tk

root = tk.Tk()
root.geometry("450x500")
root.title("Srcollbar practice")

# scroll = tk.Scrollbar(root,
#                       orient=tk.VERTICAL,
#                       command=None,          # to be set later
#                       bg="lightgray",
#                       activebackground="gray",
#                       troughcolor="white",
#                       width=15,
#                       relief="sunken")

# scroll.pack(side="right", fill="y")

# now let add a textbox
text_box = tk.Text(root, width=20, height=10, wrap="word", font=("consolas", 18))
text_box.pack()

for i in range(0, 51):
    text_box.insert("end", f"Heloo world {i}\n")

# now lets add a scrollbar!

# By these line you have created a scroll bar on root window, it will appear on vertical and command for text box
# here remember vertical comes with yview and horizontal comes with xview
scroll_bar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_box.yview)

# you have packed it; you can also pass some paraemter. but lets check the intial part frist
scroll_bar.pack()
# scroll_bar.pack(side="right", fill="y")

# Now you have created for text_box but dont configuire or add with the widget so you need to add to the widget
text_box.config(yscrollcommand=scroll_bar.set)

root.mainloop()
