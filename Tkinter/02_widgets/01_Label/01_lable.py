import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Label Showcase")
root.geometry("400x300")
root.configure(bg="lightgrey")  # Background of main window

# --- Label 1: Simple Welcome Text ---
label1 = tk.Label(
    root,
    text="Welcome to Tkinter!",       # Label text
    font=("Arial", 14),               # Font and size
    fg="black",                       # Text color
    bg="lightblue",                   # Label background color
    padx=10, pady=10,                 # Padding inside label
    relief="ridge"                    # Border style
)
label1.pack(pady=20)  # Add space above and below this label

# --- Label 2: Styled Orange Label ---
label2 = tk.Label(
    root,
    text="Styled Label Example",      # Label text
    font=("Helvetica", 18, "bold"),   # Font family, size, and weight
    fg="white",                       # Text color
    bg="orange",                      # Label background
    padx=20, pady=10,                 # Inner spacing
    relief="groove",                  # Border style
    width=25                          # Width in character units
)
label2.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
