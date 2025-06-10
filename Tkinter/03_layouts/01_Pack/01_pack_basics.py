# Pack is used to place the widget. Its the most common method that is used to pack 
# any widget. Like widget.pack() without packing the widget will not show on the window

# there are some common parameter that you pass pass on pack() method. By default it will
# place any widget to the centre of the window. So lets see what are those parameters

"""
1. side ="" means which side you want that widget. left right, top or bottom
2. anchor=
        '' use to set the which side will be the text. like if you use only side then your text will appear on the
        left side but it will it or centrer on left top; so to do that you need to use anchor its values: "n" "e" "w" "s" etc

3. fill: 
        Determines if the widget should expand to fill the space.
        Values: 'x', 'y', 'both', or None (default)
        'x' makes widget expand horizontally, 'y' vertically, 'both' in both directions. 

4. expand: 
        Boolean (True or False)
        If True, the widget expands to fill any extra space in the container.
        Works together with fill.        

5. padx and pady
        Adds external padding (space) around the widget.
        Can be a single integer (applies to both sides) or a tuple (left, right) or (top, bottom)

6. ipadx and ipady
        Adds internal padding inside the widget, increasing its size.
        Adds padding inside the widget’s border.

When and How to Apply These Parameters?
side: Use to decide the direction you want to pack your widgets. For example, a vertical menu would use side='top' for 
each item.

fill + expand: Use when you want the widget to grow and take up available space. Common in resizable windows or 
when you want buttons or text areas to stretch.

anchor: Useful when the widget is smaller than its container but you want it aligned to a particular corner or side.

padx, pady: Always use to add some breathing space so your UI doesn’t look cramped.

ipadx, ipady: Use to make buttons or labels bigger without changing the font size or image size, improving UI touch 
targets.
"""

import tkinter as tk

root = tk.Tk()
root.geometry("350x400")

sample_text = tk.Label(root, text="This is a sample text")
# without packing the text will now show
# sample_text.pack() # now it will be shown to the window. default position is 
# now we can change its position 
# sample_text.pack(side="left")
# by these parameter passed the label will show oon the left side but in centre
# so set the text on the left and top we need to use: side, anchor, and fill
# sample_text.pack(side="left", anchor='n')

# now lets add fill and expand: these two parameters are use at time a time maximum time. these are use to maination
# their size after window resize 

sample_text.pack(side="top", anchor="w")

root.mainloop()