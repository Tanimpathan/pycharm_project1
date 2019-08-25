from tkinter import *

def showTable():
    table = entry.get()
    labelText1.set(table + ' X ' + '1' + '=' + table)

    two = int(table) * 2
    labelText2.set(table + ' X ' + '2' + '=' + str(two))

    three = int(table) * 3
    labelText3.set(table + ' X ' + '3' + '=' + str(three))

    four = int(table) * 4
    labelText4.set(table + ' X ' + '4' + '=' + str(four))

    five = int(table) * 5
    labelText5.set(table + ' X ' + '5' + '=' + str(five))

    six = int(table) * 6
    labelText6.set(table + ' X ' + '6' + '=' + str(six))

    seven = int(table) * 7
    labelText7.set(table + ' X ' + '7' + '=' + str(seven))

    eight = int(table) * 8
    labelText8.set(table + ' X ' + '8' + '=' + str(eight))

    nine = int(table) * 9
    labelText9.set(table + ' X ' + '9' + '=' + str(nine))

    ten = int(table) * 10
    labelText10.set(table + ' X ' + '10' + '=' + str(ten))



root = Tk()

entry = Entry(root)
entry.pack()

Button(root, text = "Show Table", command = showTable).pack()

labelText1 = StringVar()
labelText1.set('---')
Label(root, textvariable = labelText1, bg = 'green').pack()

labelText2 = StringVar()
labelText2.set('---')
Label(root, textvariable = labelText2, bg = 'yellow').pack()

labelText3 = StringVar()
labelText3.set('---')
Label(root, textvariable = labelText3, bg = 'orange').pack()

labelText4 = StringVar()
labelText4.set('---')
Label(root, textvariable = labelText4, bg = 'blue').pack()

labelText5 = StringVar()
labelText5.set('---')
Label(root, textvariable = labelText5, bg = 'red').pack()

labelText6 = StringVar()
labelText6.set('---')
Label(root, textvariable = labelText6, bg = 'pink').pack()

labelText7 = StringVar()
labelText7.set('---')
Label(root, textvariable = labelText7, bg = 'brown').pack()

labelText8 = StringVar()
labelText8.set('---')
Label(root, textvariable = labelText8, bg = 'cyan').pack()

labelText9 = StringVar()
labelText9.set('---')
Label(root, textvariable = labelText9, bg = 'magenta').pack()

labelText10 = StringVar()
labelText10.set('---')
Label(root, textvariable = labelText10, bg = 'grey').pack()





root.mainloop()