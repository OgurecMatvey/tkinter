from tkinter import*

win = Tk()
win.geometry("400x400")
x = 80
y = 80
px = 30
py = 30
font = ("arial", 20, "bold")
frame1 = Frame(win, width=y, height=x, background='lime')
frame1.grid(row=0, column=0, padx=px, pady=py)
frame2 = Frame(win, width=y, height=x, background='lime')
frame2.grid(column=2, row=0, padx=px, pady=py)
frame3 = Frame(win, width=y, height=x, background='lime')
frame3.grid(column=0, row=2, padx=px, pady=py)
frame4 = Frame(win, width=y, height=x, background='lime')
frame4.grid(column=2, row=2, padx=px, pady=py)
l1 = Label(win, text="1", font=font, bg="lime")
l1.grid(column=0, row=0)
l2 = Label(win,text="2", font=font, bg="lime")
l2.grid(column=2, row=0)
l3 = Label(win,text="3", font=font, bg="lime")
l3.grid(column=0, row=2)
l4 = Label(win,text="4", font=font, bg="lime")
l4.grid(column=2, row=2)

win.mainloop()