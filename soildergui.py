from tkinter import *
def find():
    val = int(var1.get())
    lst =[]
    for items in range (1,val+1):
        lst.append(items)
    #print (lst)
    si = 0
    while (len(lst)!= 1):
        lst.pop(si+1)
        si = si+1
        if (si == len(lst)):
            si = 0
        if (si == len(lst) - 1):
            si = -1
    print (lst)
    str1.set(str(lst[0]))
    lab = Label (obj,text ='The last man Standing is')
    lab.place (x = 5 ,y = 80)
    lab1 = Label (obj,textvariable = str1)
    lab1.place(x= 150,y=40)

obj = Tk()
obj.geometry('400x400')
obj.title('Last Man standing')
Button1= Button(obj,text = 'Find', bg = 'black', fg = 'white', bd = '10', command = find)
Button1.place(x =50, y = 50)
var1 = StringVar()
str1 = StringVar()
box1 = Entry(obj,textvariable = var1)
box1.place(x=10, y = 10)
obj.mainloop()
