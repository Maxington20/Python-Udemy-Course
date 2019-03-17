from tkinter import *

root = Tk()

def dosomething():
    print("You clicked the button")

button1 = Button(root, text="Click Here", command=dosomething())    # will print to the console, not the window
button1.pack()

root.mainloop()