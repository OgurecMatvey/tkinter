from tkinter import *

win = Tk()
size = 80
for r in range(3):
    for c in range(3):
        if r == 1 and c == 1:
            Frame(win, width=size, height=size).grid(row=r, column=c)

        else:
            f = Frame(win, width=size, height=size, bg='lime', relief='ridge', borderwidth=15)
            f.grid(row=r, column=c)

win.mainloop()