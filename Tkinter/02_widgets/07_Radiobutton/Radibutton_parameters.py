import tkinter as tk

# define the function here
def show():
    # now as you have varibale you can get the value from that variable
    print("Your choice is : ", var.get())
    choice.config(text=f"You selected: {var.get()}")

root = tk.Tk()
root.title("RadioButton Parameters")
root.geometry("350x400")

label = tk.Label(root, text="Select your choice: ")
label.pack()

# now lets create 3 raido buttons
# radiobutton = tk.Radiobutton(root, text="Python", command=show)
# radiobutton = tk.Radiobutton(root, text="c++", command=show)
# radiobutton = tk.Radiobutton(root, text="MySql", command=show)
# radiobutton.pack()

# to use radio button we need a variable to store our ans
var = tk.StringVar()
# another thing if you dont set any defaut value then it will show all selected to avoid that
# var.set("C++")
# or you want to set it to none
var.set(None)

# that was a wrong way to create radiobutton
tk.Radiobutton(root, variable=var, value="Python", text="Python", command=show).pack()
tk.Radiobutton(root, variable=var, value="C++", text="c++", command=show).pack()
tk.Radiobutton(root, variable=var, value="MySql", text="MySql", command=show).pack()

choice = tk.Label(root, text="Your choose: ")
choice.pack()
root.mainloop()

""""
Okay ami jodi simple bangla bashay kotha boli tahole bola jay amader radio button hocche multiple choice question er moto. tomar
kache onek gula option thakbe oikhan theke jekono ekta select korte hobe; Maximum time e amader option select korte hoy like
male naki female. kon languare bangal english naki math. toh ei types er situation e amader radiobutton create korte hoy.


Radio button onno widget theke kichu ta alada in terms of impelemntation. radio button er jonno tomake age ekta varibale 
pass korte hobe; accha ami eigula list akare lekhi: 
    1. first you need to create a varibel which will all the options of that radio button.
    2. in that variable you can either make it intVar or string var
    3. you can set the var to none or any specific option otherwise when you run the program it will show all selected;
    4. Just like others you dont need to create separate varibale(yes you can) but you can directly pack the button.
    5. you can add as much as options you want.
    6. in the Radiobutton widget there are some imortant parameter that you need to pass
        a. root =
        b. text = the text of the options
        c. variable = where the values will be stored
        d. value = which values will be stroed to that variable
        e. command= what will happen when any radiobutton is clicked;
    
Shudhu ei koytai na tumi chaile for loop use koreo buttons make korte parbe. jeta amara ekhon dekhbo. ar hae jei kono widget 
tmi chaile kono specefic event e configure korte parba change korte parba. 
"""