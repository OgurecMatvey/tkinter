from tkinter import*

win = Tk()
win.geometry("800x800")
x = 100
y = 100
border = 15
frame1 = Frame(win, borderwidth=border, width=y, height=x, relief='raised', background='lime')
frame1.grid(row=0, column=0)
frame2 = Frame(win, borderwidth=border, width=300, height=x, relief='raised', background='blue')
frame2.grid(column=1, row=1)
frame3 = Frame(win, borderwidth=border, width=y, height=x, relief='raised', background='lime')
frame3.grid(column=0, row=2)
frame4 = Frame(win, borderwidth=border, width=y, height=x, relief='raised', background='lime')
frame4.grid(column=5, row=0)
frame5 = Frame(win, borderwidth=border, width=y, height=x, relief='raised', background='lime')
frame5.grid(column=5, row=2)


win.mainloop()