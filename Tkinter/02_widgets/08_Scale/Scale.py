import tkinter as tk

def show_value(val):
    print("Scale value:", val)

def set_scale_value():
    # Set the value of horizontal and vertical scales
    hor_scale.set(75)
    ver_scale.set(25)

root = tk.Tk()
root.title("Tkinter Scale Widget - Full Features")

# Horizontal scale from 0 to 100 with step size 5
hor_scale = tk.Scale(root, 
                     from_=0, to=100, 
                     orient=tk.HORIZONTAL, 
                     length=300,
                     tickinterval=20,    # Shows ticks every 20 units
                     resolution=5,       # Step size (increments)
                     label="Horizontal Scale",
                     command=show_value)
hor_scale.pack(pady=10)

# Vertical scale from -50 to 50 with step size 2
ver_scale = tk.Scale(root,
                     from_=-50, to=50,
                     orient=tk.VERTICAL,
                     length=300,
                     tickinterval=25,
                     resolution=2,
                     label="Vertical Scale",
                     command=show_value)
ver_scale.pack(side=tk.LEFT, padx=20)

# Button to programmatically set scale values
btn_set = tk.Button(root, text="Set Scale Values", command=set_scale_value)
btn_set.pack(pady=20)

root.mainloop()
