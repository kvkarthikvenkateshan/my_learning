from tkinter import *
def ipadd():
    pass
    #ipaddr = input('Enter the IP Address: ')
    val= var1.get()
    lst = val.split(".")
    count = 0
    for item in lst:
        tmp = int(item)
        if (tmp >= 0 and tmp <= 255):
            count = count +1
    if count == 4:
        result.set("Valid")
        #print ('Give IP Address is Valid')
    else:
        result.set("Invalid")
        #print ('Give IP Address is Invalid')
    
obj = Tk()
obj.geometry('400x400')
obj.title('IP Address')
lab = Label (obj,text ='Enter the IP Address: ')
lab.place (x = 10 ,y = 10)
Button1= Button(obj,text = 'Validate', bg = 'black', fg = 'white', bd = '10', command = ipadd)
Button1.place(x =50, y = 50)
var1 = StringVar()
result = StringVar()
lab = Label (obj,textvariable =result)
lab.place (x = 5 ,y = 80)
box1 = Entry(obj,textvariable = var1)
box1.place(x=125, y = 10)
obj.mainloop()
