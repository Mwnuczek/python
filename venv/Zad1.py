from tkinter import *
from tkinter import messagebox

x=0

def show_entry_fields ():
    messagebox.showinfo( "Message ",'Dowolny komunikat ')
def chngeColor():
    val = var1.get()
    print ('color change')
    print (val)
    if val==1:
        b1.config(bg="red")
    if val==2:
        b1.config(bg="green")
    if val==3:
        b1.config(bg="blue")

master=Tk()

var1 = IntVar()
b1=Button(master, text ='button' , command = show_entry_fields)
b1.pack()

r1=Radiobutton ( master ,text = " red " ,variable=var1, value =1, command = chngeColor)
r2=Radiobutton ( master ,text = " green " ,variable=var1,value =2, command = chngeColor)
r3=Radiobutton ( master ,text = " blue " ,variable=var1,value =3, command = chngeColor)
r1.pack()
r2.pack()
r3.pack()

master.mainloop()

'''
def add(ent,y):
    global x
    x += y
    ent.delete(0,'end')
    ent.insert(END, str(x))
'''