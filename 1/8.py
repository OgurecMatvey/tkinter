from tkinter import *

win = Tk()
original_img = PhotoImage(file="a.png")
small_img = original_img.subsample(3, 3)
Label(win, image=small_img, text="Кофе?", font=("Arial", 16), compound="top").pack(pady=20)
#bottom left top
win.mainloop()