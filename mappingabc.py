from tkinter import *

def disp(key):
    d = {'a':'Avengers','b':'Batman','c':'Captian America','d':'Dragons','e':'elite','f':'Fantstic 4','g':'Game','h':'Hulk','i':'Indian Johnes','j':'Johnny','k':'Karthik','l':'Lucky','m':'main','n':'Nagashree','o':'orange','p':'Prathibha','q':'Queen','r':'Ritisha','s':'shree','t':'Tommy','u':'Uber','v':'Volverine','w':'white collar','x':'X-men','y':'Yorker','z':'Zero',}
    val = d.get(key)
    ent.delete(0,END)
    ent.insert(0,val)


obj = Tk()
obj.title('Mapp')
alpa = StringVar() 

frame6 = Frame(obj)# creates a frame
frame6.pack(side = BOTTOM)# pushes the frame to the bottom

but26= Button (frame6,padx =16, pady=16, bd =8, text ="Z",command = lambda:disp('z'), fg = 'black')
but26.pack(side = RIGHT)

frame5 = Frame(obj)# creates a frame
frame5.pack(side = BOTTOM)# pushes the frame to the bottom

but21 = Button (frame5,padx =16, pady=16, bd =8, text ="U",command = lambda:disp('u'), fg = 'black')
but21.pack(side = LEFT)
but22 = Button (frame5,padx =16, pady=16, bd =8, text ="V",command = lambda:disp('v'), fg = 'black')
but22.pack(side = LEFT)
but23 = Button (frame5,padx =16, pady=16, bd =8, text ="W",command = lambda:disp('w'),fg = 'black')
but23.pack(side = LEFT)
but24 = Button (frame5,padx =16, pady=16, bd =8, text ="X",command = lambda:disp('x'), fg = 'black')
but24.pack(side = LEFT)
but25 = Button (frame5,padx =16, pady=16, bd =8, text ="Y",command = lambda:disp('y'), fg = 'black')
but25.pack(side = LEFT)

frame4 = Frame(obj)# creates a frame
frame4.pack(side = BOTTOM)# pushes the frame to the bottom

but16 = Button (frame4,padx =16, pady=16, bd =8, text ="P",command = lambda:disp('p'), fg = 'black')
but16.pack(side = LEFT)
but17 = Button (frame4,padx =16, pady=16, bd =8, text ="Q",command = lambda:disp('q'), fg = 'black')
but17.pack(side = LEFT)
but18 = Button (frame4,padx =16, pady=16, bd =8, text ="R",command = lambda:disp('r'),fg = 'black')
but18.pack(side = LEFT)
but19 = Button (frame4,padx =16, pady=16, bd =8, text ="S",command = lambda:disp('s'), fg = 'black')
but19.pack(side = LEFT)
but20 = Button (frame4,padx =16, pady=16, bd =8, text ="T",command = lambda:disp('t'), fg = 'black')
but20.pack(side = LEFT)


frame3 = Frame(obj)# creates a frame
frame3.pack(side = BOTTOM)# pushes the frame to the bottom

but11 = Button (frame3,padx =16, pady=16, bd =8, text ="K",command = lambda:disp('k'), fg = 'black')
but11.pack(side = LEFT)
but12 = Button (frame3,padx =16, pady=16, bd =8, text ="L",command = lambda:disp('l'), fg = 'black')
but12.pack(side = LEFT)
but13 = Button (frame3,padx =16, pady=16, bd =8, text ="M",command = lambda:disp('m'),fg = 'black')
but13.pack(side = LEFT)
but14 = Button (frame3,padx =16, pady=16, bd =8, text ="N",command = lambda:disp('n'), fg = 'black')
but14.pack(side = LEFT)
but15 = Button (frame3,padx =16, pady=16, bd =8, text ="O",command = lambda:disp('o'), fg = 'black')
but15.pack(side = LEFT)

frame2 = Frame(obj)# creates a frame
frame2.pack(side = BOTTOM)# pushes the frame to the bottom

but6 = Button (frame2,padx =16, pady=16, bd =8, text ="F",command = lambda:disp('f'), fg = 'black')
but6.pack(side = LEFT)
but7 = Button (frame2,padx =16, pady=16, bd =8, text ="G",command = lambda:disp('g'), fg = 'black')
but7.pack(side = LEFT)
but8 = Button (frame2,padx =16, pady=16, bd =8, text ="H",command = lambda:disp('h'), fg = 'black')
but8.pack(side = LEFT)
but9 = Button (frame2,padx =16, pady=16, bd =8, text ="I",command = lambda:disp('i'), fg = 'black')
but9.pack(side = LEFT)
but10 = Button (frame2,padx =16, pady=16, bd =8, text ="J",command = lambda:disp('j'), fg = 'black')
but10.pack(side = LEFT)


frame1 = Frame(obj)# creates a frame
frame1.pack(side = BOTTOM)# pushes the frame to the bottom

but1 = Button (frame1,padx =16, pady=16, bd =8, text ="A",command = lambda:disp('a'), fg = 'black')
but1.pack(side = LEFT)
but2 = Button (frame1,padx =16, pady=16, bd =8, text ="B",command = lambda:disp('b'), fg = 'black')
but2.pack(side = LEFT)
but3 = Button (frame1,padx =16, pady=16, bd =8, text ="C",command = lambda:disp('c'), fg = 'black')
but3.pack(side = LEFT)
but4 = Button (frame1,padx =16, pady=16, bd =8, text ="D",command = lambda:disp('d'), fg = 'black')
but4.pack(side = LEFT)
but5 = Button (frame1,padx =16, pady=16, bd =8, text ="E",command = lambda:disp('e'), fg = 'black')
but5.pack(side = LEFT)

frame0 = Frame(obj)# creates a frame
frame0.pack(side = BOTTOM)# pushes the frame to the Top
ent = Entry (frame0, textvariable = alpa, bd = 20, insertwidth =1, font = 30)
ent.pack(side = TOP)

obj.mainloop()