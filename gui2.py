from tkinter import *
def calc(m):
    #pass
    val1 = var1.get()
    val2 = var2.get()
    if m == "Ad":
        result.set(val1 + val2)
    elif m == "Sub":
        result.set(val1 - val2)
    elif m == "MU":
        result.set(val1 * val2)
    elif m == "Di":
        result.set(val1/val2)
    lab1 = Label(obj,textvariable = result)
    lab1.place(x = 60,y = 120)
obj = Tk()
obj.geometry('400x400')
obj.title('Calculator')
Button1= Button(obj,text = 'Add', bg = 'black', fg = 'white', bd = '10', command = lambda:calc("Ad"))
Button1.place(x =10, y = 10)
Button2= Button(obj,text = 'Sub', bg = 'black', fg = 'white', bd = '10', command = lambda:calc("Sub"))
Button2.place(x =60, y = 10)
Button3 = Button (obj,text = 'Mul', bg = 'black', fg = 'white', bd = '10', command = lambda:calc("MU"))
Button3.place(x=110, y=10)
Button4 = Button (obj,text = 'Div', bg = 'black', fg = 'white', bd = '10', command = lambda:calc("Di"))
Button4.place(x=160, y=10)
var1 = IntVar()
var2 = IntVar()
result= IntVar()
box1 = Entry(obj,textvariable = var1)
box1.place(x=60, y = 60)
box2 = Entry(obj,textvariable = var2)
box2.place(x=60, y = 90)
lab2 = Label(obj,text="value 1:")
lab2.place(x=10,y=60)
lab3 = Label(obj,text="value 2:")
lab3.place(x=10,y=90)
obj.mainloop()