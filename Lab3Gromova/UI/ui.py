from tkinter import *
from tkinter.ttk import *
import tkinter


window = Tk()
window.title("meow")
window.geometry('700x600')

LabelFrame_5 = tkinter.LabelFrame(window,text="Параметры задачи",takefocus = True,width = 10,height = 4)
LabelFrame_5.place(x = 340,y = 19,width = 338,height = 259)
LabelFrame_5.configure(relief = "groove")


Button_9 = tkinter.Button(window,text="Вычислить!",width = 10,height = 4)
Button_9.place(x = 49,y = 169,width = 234,height = 87)

Label_6 = tkinter.Label(LabelFrame_5,text="Начало диапазона(а)",width = 10,height = 4)
Label_6.place(x = 21,y = 28,width = 121,height = 40)
Label_6.configure(anchor = "w")
Label_6.configure(relief = "flat")

Label_7 = tkinter.Label(LabelFrame_5,text="Конец диапазона(b)",width = 10,height = 4)
Label_7.place(x = 21,y = 64,width = 111,height = 45)
Label_7.configure(anchor = "w")
Label_7.configure(relief = "flat")

Label_8 = tkinter.Label(LabelFrame_5,text="Шаг(h)",width = 10,height = 4)
Label_8.place(x = 23,y = 109,width = 109,height = 35)
Label_8.configure(anchor = "w")
Label_8.configure(relief = "flat")

Entry_12 = tkinter.Entry(LabelFrame_5)
Entry_12.place(x = 157,y = 74,width = 120,height = 20)
Entry_12.configure(relief = "sunken")

Entry_13 = tkinter.Entry(LabelFrame_5)
Entry_13.place(x = 157,y = 113,width = 120,height = 20)
Entry_13.configure(relief = "sunken")

Entry_17 = tkinter.Entry(LabelFrame_5)
Entry_17.place(x = 157,y = 35,width = 120,height = 20)
Entry_17.configure(relief = "sunken")

window.mainloop()

