from tkinter import *
winodw = Tk()

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
x=0
winodw.title("TIC-TAC-TOE")
winodw.rowconfigure(1,weight=1,minsize=100)
winodw.columnconfigure(1,weight=1,minsize=100)
#its a reset button that changes everytthing to start of game 
def end():
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            var6.set("")
            var7.set("")
            var8.set("")
            var9.set("")
            global x
            global a
            global b
            global c
            global d
            global e
            global f
            global g
            global h
            global i
            a=0
            b=0
            c=0
            d=0
            e=0
            f=0
            g=0
            h=0
            i=0
            x=0
            l1.configure(relief=GROOVE)
            l2.configure(relief=GROOVE)
            l3.configure(relief=GROOVE)
            l4.configure(relief=GROOVE)
            l5.configure(relief=GROOVE)
            l6.configure(relief=GROOVE)
            l7.configure(relief=GROOVE)
            l8.configure(relief=GROOVE)
            l9.configure(relief=GROOVE)
            var10.set("")
            var11.set("")
# below all g function are made to check if the label is blank or not if blank
#then set var =1 and it helps us in win condition 
def g1():
    global a
    a=1
    l1.configure(relief=RAISED)
def g2():
    global b
    b=1
    l2.configure(relief=RAISED)
def g3():
    global c
    c=1
    l3.configure(relief=RAISED)
def g4():
    global d
    d=1
    l4.configure(relief=RAISED)
def g5():
    global e
    e=1
    l5.configure(relief=RAISED)
def g6():
    global f
    f=1
    l6.configure(relief=RAISED)
def g7():
    global g
    g=1
    l7.configure(relief=RAISED)
def g8():
    global h
    h=1
    l8.configure(relief=RAISED)
def g9():
    global i
    i=1
    l9.configure(relief=RAISED)

#this is the function where we check the winning condition and prints win on lable 
def win():
      if(l1.cget("text")==l2.cget("text")==l3.cget("text")and a!=0 and b!=0 and c!=0):
            var10.set("WIN")
      elif(l4.cget("text")==l5.cget("text")==l6.cget("text")and d!=0 and e!=0 and f!=0):
            var10.set("WIN")
      elif(l1.cget("text")==l4.cget("text")==l7.cget("text")and a!=0 and d!=0 and g!=0):
            var10.set("WIN") 
      elif(l7.cget("text")==l8.cget("text")==l9.cget("text")and g!=0 and h!=0 and i!=0):
            var10.set("WIN") 
      elif(l2.cget("text")==l5.cget("text")==l8.cget("text")and b!=0 and e!=0 and h!=0):
            var10.set("WIN")     
      elif(l3.cget("text")==l6.cget("text")==l9.cget("text")and c!=0 and f!=0 and i!=0):
            var10.set("WIN")
      elif(l1.cget("text")==l5.cget("text")==l9.cget("text")and a!=0 and e!=0 and i!=0):
            var10.set("WIN")
      elif(l3.cget("text")==l5.cget("text")==l7.cget("text")and c!=0 and e!=0 and g!=0):
            var10.set("WIN")

#this handles the main running of thing as all label somes here first
def handle(event,n,g,q):
    global x;
    if g10.cget("text")=="WIN":
        var11.set("CLEAR\nSCREEN")
        
    elif q!=1 :
        g()
        if x==0:
            n.set("X")
            x=1
            win()   
        else:
            n.set("0")
            x=0
            win()
#this variable sets the text of all labels     
var1=StringVar()      
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=StringVar()
var11=StringVar()

# here we have declared all the widgets
l1= Label(winodw,textvariable=var1,fg="white",bg="grey",width=8,height=6,relief=GROOVE)
l1.grid(row=0,column=0,padx=10,pady=10)
l2= Label(winodw,fg="white",bg="grey",textvariable=var2,width=8,height=6,relief=GROOVE)
l2.grid(row=0,column=1,padx=10,pady=10)
l3= Label(winodw,fg="white",bg="grey",textvariable=var3,width=8,height=6,relief=GROOVE)
l3.grid(row=0,column=2,padx=10,pady=10)
l4= Label(winodw,fg="white",bg="grey" ,textvariable=var4,width=8,height=6,relief=GROOVE)
l4.grid(row=1,column=0,padx=10,pady=10)
l5= Label(winodw ,fg="white",bg="grey",textvariable=var5,width=8,height=6,relief=GROOVE)
l5.grid(row=1,column=1,padx=10,pady=10)
l6= Label(winodw,fg="white",bg="grey",textvariable=var6,width=8,height=6,relief=GROOVE)
l6.grid(row=1,column=2,padx=10,pady=10)
l7= Label(winodw ,fg="white",bg="grey",textvariable=var7,width=8,height=6,relief=GROOVE)
l7.grid(row=2,column=0,padx=10,pady=10)
l8= Label(winodw,fg="white",bg="grey",textvariable=var8,width=8,height=6,relief=GROOVE)
l8.grid(row=2,column=1,padx=10,pady=10)
l9= Label(winodw,fg="white",bg="grey",textvariable=var9,width=8,height=6,relief=GROOVE)
l9.grid(row=2,column=2,padx=10,pady=10)
g10=Label(winodw,fg='black',bg='yellow',width=4,height=2,textvariable=var10)
g10.grid(row=4,column=1,padx=15,pady=15,sticky="news")
g11=Button(winodw,fg='white',bg='black',width=5,height=3,command=end,text="RESET")
g11.grid(row=4,column=2,padx=15,pady=15)
g12=Label(winodw,fg='black',bg='lightblue',width=6,height=1,textvariable=var11)
g12.grid(row=4,column=0,padx=15,pady=15,sticky="news")


# and here all the binding happens 
l1.bind("<Button>", lambda event, n='var1',g='g1',q='a': handle(event, var1, g1, a))
l2.bind("<Button>", lambda event, n='var2',g='g2',q='b': handle(event, var2, g2, b))
l3.bind("<Button>", lambda event, n='var3',g='g3',q='c': handle(event, var3, g3, c))
l4.bind("<Button>", lambda event, n='var4',g='g4',q='d': handle(event, var4, g4, d))
l5.bind("<Button>", lambda event, n='var5',g='g5',q='e': handle(event, var5, g5, e))
l6.bind("<Button>", lambda event, n='var6',g='g6',q='f': handle(event, var6, g6, f))
l7.bind("<Button>", lambda event, n='var7',g='g7',q='g': handle(event, var7, g7, g))
l8.bind("<Button>", lambda event, n='var8',g='g8',q='h': handle(event, var8, g8, h))
l9.bind("<Button>", lambda event, n='var9',g='g9',q='i': handle(event, var9, g9, i))



winodw.mainloop()
