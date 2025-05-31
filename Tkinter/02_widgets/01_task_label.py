import tkinter as tk
root = tk.Tk()
root.title("Label task 1")
root.geometry("450x500")

label1 = tk.Label(
    root, 
    text="this is lable 1",
    font=("Monaco", 24),
    bg = "red"
)
label1.pack(padx=10, pady=10)

# tobe tumi chaile 1 line e o likhte paro.
label2 = tk.Label(root, text="This is lable 2", font=("Arial", 30), fg="Blue")
label2.pack()
root.mainloop()