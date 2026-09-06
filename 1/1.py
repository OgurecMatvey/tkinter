from tkinter import*

win = Tk()
#win.geometry("800x800")
x = 30
border = 3
frame1 = Frame(win, borderwidth=border, width=600, height=x, relief='raised', background='red')
frame1.grid(row=0, column=0)
frame2 = Frame(win, borderwidth=border, width=600, height=x, relief='raised', background='orange')
frame2.grid(column=0, row=1)
frame3 = Frame(win, borderwidth=border, width=600, height=x, relief='raised', background='yellow')
frame3.grid(column=0, row=2)
frame4 = Frame(win, borderwidth=border, width=600, height=x, relief='raised', background='green')
frame4.grid(column=0, row=3)
frame5 = Frame(win, borderwidth=border, width=600, height=x, relief='raised', background='light blue')
frame5.grid(column=0, row=4)
frame6 = Frame(win, borderwidth=border, width=600, height=x, relief='raised', background='blue')
frame6.grid(column=0, row=5)
frame7 = Frame(win, borderwidth=border, width=600, height=x, relief='raised', background='violet')
frame7.grid(column=0, row=6)


win.mainloop()
