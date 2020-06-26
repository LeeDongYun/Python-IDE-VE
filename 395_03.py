from tkinter import *


def setstr(txt):
    data.delete(0, "end")
    data.insert(0, txt)

str = ['파이썬','코틀린']


win = Tk()
data = Entry(win)
data.grid(row=0, column=0,columnspan=2)

py = Button (win, text=str[0], command = lambda: setstr(str[0]))
py.grid(row=1,column=0)
ko = Button (win, text=str[1], command = lambda: setstr(str[1]))
ko.grid(row=1,column=1)

win.mainloop()