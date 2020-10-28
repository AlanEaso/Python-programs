#Miles to Kilometers Converter

from tkinter import *

def convert():
    c= int(milevalue.get())
    c *= 1.60934
    f = "Kilometers:" + str(c)
    Label(win,text=f).grid(row=6,column=3)

win = Tk()

win.geometry('200x150')

Label(win,text="Miles To Kilometers",pady=15).grid(column=3)

miles = Label(win,text="Miles:")

miles.grid(row=1,column=2)

milevalue= DoubleVar()

mileentry=Entry(win,textvariable=milevalue)

mileentry.grid(row=1,column=3)

Button(text="Convert",command=convert).grid(row=4,column=3)

win.mainloop()