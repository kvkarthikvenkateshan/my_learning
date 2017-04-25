from tkinter import *
def letter(m):
    #pass
    dic = {'a':'Avengers','b':'Batman','c':'Captian America','d':'Dragons'}
    val = var1.get(m)
    tmp = dic.get(val)
    result.set(tmp)
    #inp = input ('Enter an Alphabet from a to d: ')
    #print (dic.get(inp))
obj = Tk()
obj.geometry('400x400')
obj.title('Letter to Word')
var1 = StringVar()
result = StringVar()
lab = Label (obj,textvariable =result)
lab.place (x = 100 ,y = 80)
Button1= Button(obj,text = 'A', bg = 'black', fg = 'white', bd = '10', command = letter(m))
Button1.place(x =10, y = 50)
box1 = Entry(obj,textvariable = var1)
box1.place(x=160, y = 10)
obj.mainloop()
