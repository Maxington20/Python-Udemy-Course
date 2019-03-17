from tkinter import *

class MyButtons:

    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="Click Here", command=self.printmessage)  # do not include the () after
                                                                                        # the method (printmessage)
        self.printbutton.pack()

        self.quitbotton = Button(frame, text="Exit", command=frame.quit)    # quit method will close the window
        self.quitbotton.pack(side=LEFT)

    def printmessage(self):
        print("Button Clicked")


root = Tk()

b = MyButtons(root)

root.mainloop()