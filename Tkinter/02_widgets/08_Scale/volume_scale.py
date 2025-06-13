import tkinter as tk
from tkinter import ttk

def update_volume(val):
    volume = int(val)
    volume_label.config(text=f"Volume: {volume}%")
    volume_bar['value'] = volume

    # Optional: Change color based on volume level
    if volume < 30:
        volume_bar.configure(style="Low.Horizontal.TProgressbar")
    elif volume < 70:
        volume_bar.configure(style="Medium.Horizontal.TProgressbar")
    else:
        volume_bar.configure(style="High.Horizontal.TProgressbar")

root = tk.Tk()
root.title("Volume Simulator")
root.geometry("400x200")
root.resizable(False, False)

# Style for progress bar (volume indicator)
style = ttk.Style(root)
style.theme_use('clam')

style.configure("Low.Horizontal.TProgressbar", foreground='green', background='green')
style.configure("Medium.Horizontal.TProgressbar", foreground='orange', background='orange')
style.configure("High.Horizontal.TProgressbar", foreground='red', background='red')

# Label
volume_label = tk.Label(root, text="Volume: 50%", font=("Arial", 14))
volume_label.pack(pady=10)

# Progress bar
volume_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate', maximum=100)
volume_bar.pack(pady=10)
volume_bar['value'] = 50  # initial volume

# Scale widget for volume control
volume_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=300,
                        resolution=1, command=update_volume)
volume_scale.set(50)
volume_scale.pack()

root.mainloop()
