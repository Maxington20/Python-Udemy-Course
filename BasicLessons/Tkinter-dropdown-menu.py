from tkinter import *

def function1():
    print("Menu item clicked")

root = Tk()

mymenu = Menu(root) # main menu
root.config(menu=mymenu)    # tells python this is the menu we are using right now

submenu = Menu(mymenu)  # passing submenu into the main menu
submenu2 = Menu(mymenu)
mymenu.add_cascade(label="File", menu=submenu)  # adding a dropdown to the main menu

submenu.add_command(label="Project", command=function1) # Adding a submenu item
submenu.add_command(label="Save", command=function1)    # Adding another submenu item

submenu.add_separator() # add a separator between menu items

submenu.add_command(label="Exit", command=quit) # Add another submenu item that will close the program

newmenu = Menu(mymenu)  # creating a second submenu
mymenu.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="Undo", command=function1)

root.mainloop()