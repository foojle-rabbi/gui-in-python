import tkinter as tk

root = tk.Tk()
root.title("checking destroy function")
root.geometry("350x400")


# ooh wow its a great method to quit from a window. command only works when a button is clicked
a_button = tk.Button(root, text="Quit", command=root.destroy)
a_button.pack()

root.mainloop()