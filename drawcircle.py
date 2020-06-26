from random import randrange
from tkinter import *

def escapemouse(e):
    w = win.winfo_width()
    h = win.winfo_heigh()
    print('윈도우 크기: ',w,h)

    bw = btn.winfo_width()
    bn = btn.winfo_heigh()
    print('버튼 크기:', bw, bh)

    rx = randrange(0, w - bw)
    ry = randrange(0, h - bh)

    print('이동 위치', rx, ry)
    btn.place(x=rx, y=ry)

------------------------------------------------------------------------------------------------\\win = Tk()
win.geometry("600x300+100+100")
win.title('마우스를 도망가는 버튼')
win.resizable(False,False)

btn = Button(win, text='저를 눌러보세요', command =win.quit)

btn.place(x=200,y=30)

btn.bind('<Enter>',escapemouse)

win.mainloop()
-