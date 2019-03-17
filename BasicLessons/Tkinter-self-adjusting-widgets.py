from tkinter import *

root = Tk()

label1 = Label(root, text="First Name", bg="Red", fg="White")
label1.pack(fill=X) # fill this label to the width of the window

label2 = Label(root, text="Second", bg="Blue", fg="Green")
label2.pack(side=LEFT, fill=Y)

root.mainloop()