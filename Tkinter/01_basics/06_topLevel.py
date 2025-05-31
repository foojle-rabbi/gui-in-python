import tkinter as tk

def onClick():
    second_window = tk.Toplevel(root)
    second_window.title("Second window")
    second_window.geometry("250x300")

    # eikhane ekta prolbem ache sheta holo 2nd window open holeo 1st window kaj kore. sehta off koar jonno
    

root = tk.Tk()
root.title("First window")
root.geometry("350x400")

button_for_second_win = tk.Button(root, text="2nd window", command=onClick)
button_for_second_win.pack()

root.mainloop()