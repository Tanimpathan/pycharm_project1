from tkinter import *


def changToRed():
    labeltext.set('Red')
    mylabel.config(bg = 'red')

def changeToGreen():
    labeltext.set('Green')
    mylabel.config(bg = 'green')

def changeToBlue():
    labeltext.set('Blue')
    mylabel.config(bg = 'blue')



root = Tk()
labeltext = StringVar()
labeltext.set('label')

mylabel = Label(root, textvariable = labeltext)
mylabel.pack()

Button(root, text = "Red", command = changToRed).pack()
Button(root, text = "Green", command = changeToGreen).pack()
Button(root, text = "Blue", command = changeToBlue).pack()


root.mainloop()

