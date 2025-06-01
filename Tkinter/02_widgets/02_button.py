import tkinter as tk
from tkinter import messagebox

# so now we need to define the when_clicked function
def when_clicked():
    print("the Second button has clicked") # but this messeage will be seen to the terminal
    # so if we want to show the messeage in a message box we need to import messeage box

    # messagebox.showinfo("You clicked the button with command")

    # ------ Lets see if my custom popup window works or not
    my_custom_popup("My custom popup", "Hello Fojle")
    # Yes bro it works just like butter. 

    # Accha showinfo 2 ta parameter ney first one is the title second is the information so 
    messagebox.showinfo("Messagebox", "You clicked the button with command")

    # now I have some question can i change the size(widthxheight) of messagebox? 
    # yes I know anotehr thing that i can create another winow when the second button is clicked so on that window
    # i could easily resize give title anything can be done. but what about messagebox?

    # ------------- ans of this qeustion ------------------------
    """
    About your messagebox size question:
    The standard Tkinter messagebox dialogs (like showinfo, showwarning, showerror, etc.) do NOT allow you to 
    directly control their size or geometry. These dialogs are managed by the underlying system and are meant
    to have a consistent look and feel across applications.

    If you want a custom-sized popup, you should create a custom Toplevel window (a new window), then add your
    own widgets, buttons, and customize the size, title, and behavior exactly as you want.
    """
# ----------- here is the custom pop up message box function
def custom_popup():
    popup = tk.Toplevel(root)
    popup.title("Custom Popup")
    popup.geometry("300x150")
    label = tk.Label(popup, text="This is a custom popup window!")
    label.pack(pady=20)
    btn_close = tk.Button(popup, text="Close", command=popup.destroy)
    btn_close.pack(pady=10)



# hey there if this is the scence that means i could create my own messeage box, i just simply define a fucntion
# what will create the title, size, the error message? yes I think its possbiel lets try this:
def my_custom_popup(title, information):
    popup_window = tk.Toplevel(root)
    popup_window.title(title)
    popup_window.geometry("250x400")

    # tk.Label(popup_window, text="information").pack(pady=20) #eikhane ekta vul hoiche text e value pass korte hobe
    tk.Label(popup_window, text=information).pack(pady=20)
    tk.Button(popup_window, text="Close", command=popup_window.destroy).pack(pady=30)


# Create the main window
root = tk.Tk()
root.title("Button Example")
root.geometry("300x200")
root.configure(bg="white")  # Set background color for the main window

# --- Button 1: Simple Button ---
button1 = tk.Button(
    root,
    text="Click Me!",          # Text displayed on the button
    font=("Arial", 12),        # Font family and size
    fg="black",                # Text color
    bg="lightgreen",           # Button background color
    padx=10, pady=5,           # Padding inside the button (left-right, top-bottom)
    relief="raised"            # Border style for the button
)
button1.pack(pady=20)          # Add vertical space above and below the button

# the button we have created is a simple button which does nothing when clicked. to add something we need to
# --- Button 2: Button with program ---
button2 = tk.Button(root, text="Button with command", command=when_clicked)
# so we have created a second button named button with command so when we click on that the when_clicked fucntion will called
button2.pack()

# Start the Tkinter main loop
root.mainloop()
