from tkinter import *   # This imports everything from tkinter

root = Tk() # object of tk class called root

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="Click here", fg="Red")
button2 = Button(otherframe, text="Click here", fg="Blue")

button1.pack()
button2.pack()


root.mainloop() # causes window to only close when we tell it to by clicking the button on the window to close