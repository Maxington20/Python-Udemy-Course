from tkinter import *   # This imports everything from tkinter

root = Tk() # object of tk class called root

label1 = Label(root, text="Hello World")    # object of label class, pass in root, and text to display

label1.pack()

root.mainloop() # causes window to only close when we tell it to