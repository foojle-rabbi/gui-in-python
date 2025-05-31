import tkinter as tk

def open3rd():
    window_3rd = tk.Toplevel(second_window)
    window_3rd.title("This is the 3rd window")
    window_3rd.geometry("400x500")
    tk.Label(window_3rd, text="This is on 3rd window").pack()
    # upoer line ta dekhcho. ami chaile variable decalre na kore direct o korte parum.

    #now lets try the destroy and quit fucntion
    tk.Button(window_3rd, text="Destry", command=window_3rd.destroy).pack()
    # okay that means destroy will quit all the windows.

root = tk.Tk()
root.title("This is the main window")
root.geometry("350x400")

second_window = tk.Toplevel(root)
second_window.title("Second window")
second_window.geometry("250x300")

lebel_root = tk.Label(root, text="This is for root window")
lebel_root.pack()

lebel_second = tk.Label(second_window, text="this is for second window")
lebel_second.pack()

#yes its possible to create multiple window. you can also do with a button
second_window_button = tk.Button(second_window, text="open 3rd window", command=open3rd)
# button ami pack kori nai jar karone show hoy nai.
second_window_button.pack()

root.mainloop()