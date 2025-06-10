import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a Text widget
text_widget = tk.Text(root, wrap="none")
text_widget.pack(side="left", fill="both", expand=True)

# Create a vertical scrollbar and connect it to the Text widget
scrollbar = tk.Scrollbar(root, orient="vertical", command=text_widget.yview)
scrollbar.pack(side="right", fill="y")

# Attach the scrollbar to the Text widget
text_widget.config(yscrollcommand=scrollbar.set)

# Add lots of text for scrolling
for i in range(100):
    text_widget.insert("end", f"Line {i+1}\n")

root.mainloop()
