from tkinter import *

win = Tk()
x = 80
original_img = PhotoImage(file="a.png")
small_img = original_img.subsample(3, 3)

for r in range(3):
    for c in range(3):
        if r == 1 and c == 1:
            Label(win, image=small_img).grid(row=r, column=c)

        else:
            f = Frame(win, width=x, height=x, bg='lime', relief='ridge', borderwidth=15)
            f.grid(row=r, column=c, padx=60, pady=60)

win.mainloop()