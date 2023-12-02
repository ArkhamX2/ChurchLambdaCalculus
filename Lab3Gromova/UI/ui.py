from tkinter import *
from tkinter.ttk import *
import tkinter
import numpy as np
from tkinter import PhotoImage

def button_click():
    a = float(Entry_a.get())
    b = float(Entry_b.get())
    h = float(Entry_h.get())
    res = []
    for x in np.arange(a,b,h):
        res.append(x**4 + x*2 + x + 1)
    counter = 1
    for i in np.arange(a,b+h,h):
        TreeViewMeow.insert(counter, "meow", i=i)
        counter +=1
    meow =[(1,1,1),(2,2,2),(2,1,3)]
    for x in meow:
        TreeViewMeow.insert("", END, values=x)
    TreeViewMeow.update_idletasks()    
    

window = Tk()
window.title("meow")
window.geometry('700x600')

photo = tkinter.PhotoImage(file="Screenshot_3.png")
label = tkinter.Label(image=photo)
label.place(x = 10,y = 19, width = 320,height = 135)

LabelFrameMeow = tkinter.LabelFrame(window,text="Параметры задачи",takefocus = True,width = 10,height = 4)
LabelFrameMeow.place(x = 340,y = 19,width = 338,height = 259)
LabelFrameMeow.configure(relief = "groove")

ButtonMeow = tkinter.Button(window,text="Вычислить!",width = 10,height = 4, comman=button_click)
ButtonMeow.place(x = 10,y = 169,width = 320,height = 107)

Label_a = tkinter.Label(LabelFrameMeow,text="Начало диапазона(а)",width = 10,height = 4)
Label_a.place(x = 21,y = 28,width = 121,height = 40)
Label_a.configure(anchor = "w")
Label_a.configure(relief = "flat")

Label_b = tkinter.Label(LabelFrameMeow,text="Конец диапазона(b)",width = 10,height = 4)
Label_b.place(x = 21,y = 64,width = 111,height = 45)
Label_b.configure(anchor = "w")
Label_b.configure(relief = "flat")

Label_h = tkinter.Label(LabelFrameMeow,text="Шаг(h)",width = 10,height = 4)
Label_h.place(x = 23,y = 109,width = 109,height = 35)
Label_h.configure(anchor = "w")
Label_h.configure(relief = "flat")

Label_F = tkinter.Label(LabelFrameMeow,text="Функция: f(x) = x^4 + x^2 + x + 1",width = 10,height = 4)
Label_F.place(x = 23,y = 150,width = 200,height = 35)
Label_F.configure(anchor = "w")
Label_F.configure(relief = "flat")

Entry_a = tkinter.Entry(LabelFrameMeow)
Entry_a.place(x = 157,y = 74,width = 120,height = 20)
Entry_a.configure(relief = "sunken")

Entry_b = tkinter.Entry(LabelFrameMeow)
Entry_b.place(x = 157,y = 113,width = 120,height = 20)
Entry_b.configure(relief = "sunken")

Entry_h = tkinter.Entry(LabelFrameMeow)
Entry_h.place(x = 157,y = 35,width = 120,height = 20)
Entry_h.configure(relief = "sunken")

columns = ("#1", "#2", "#3")
TreeViewMeow = tkinter.ttk.Treeview(window,show="headings",columns=columns)
TreeViewMeow.place(x = 10,y = 300,width = 669,height = 280)
TreeViewMeow.configure(selectmode = "extended")
ysb = tkinter.ttk.Scrollbar(TreeViewMeow, orient=tkinter.HORIZONTAL, command=TreeViewMeow.yview)
TreeViewMeow.configure(yscroll=ysb.set)
TreeViewMeow.heading("#1", text="№")
TreeViewMeow.heading("#2", text="X")
TreeViewMeow.heading("#3", text="f(X)")

window.mainloop()

