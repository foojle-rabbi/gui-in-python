# Importing tkinter library
import tkinter as tk  # 'tk' is an alias for easier reference

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("My First Tkinter App")

# Set the size of the window: width x height
root.geometry("400x300")

# Optional: Set the background color of the window
root.configure(bg="green")

# This is the main loop of the application
# It keeps the window open and waits for user interaction
root.mainloop()
