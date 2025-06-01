import tkinter as tk

def on_entry_click(event):
    if entry.get() == 'Enter your name':
        entry.delete(0, tk.END)  # Clear placeholder text
        entry.config(fg='black')

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter your name')  # Put placeholder back
        entry.config(fg='grey')

def submit():
    text = entry.get()
    if text == 'Enter your name' or text == '':
        print("Please enter your name!")
    else:
        print(f"You entered: {text}")
        entry.delete(0, tk.END)
        entry.insert(0, 'Enter your name')
        entry.config(fg='grey')

root = tk.Tk()
root.geometry('300x150')
root.title('Entry with Placeholder')

entry = tk.Entry(root, fg='grey')
entry.insert(0, 'Enter your name')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack(pady=20)

submit_btn = tk.Button(root, text='Submit', command=submit)
submit_btn.pack()

root.mainloop()
