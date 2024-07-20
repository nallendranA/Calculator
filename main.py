from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as m
class file:
    def __init__(self,c):
        style=Style()
        style.theme_use('clam')
        style.configure('l.Label',font=('ArielBlack',16))
        self.l=Label(c,text='Simple Calculator',style='l.Label')
        self.l1=Label(c,text='First Number')
        self.l2=Label(c,text='Second Number')
        self.l3=Label(c,text='Result')
        self.e1=Entry()
        self.e2=Entry()
        self.e3=Entry()
        self.l1.place(x=100,y=50)
        self.l2.place(x=100,y=100)
        self.e1.place(x=200,y=50)
        self.e2.place(x=200,y=100)
        self.b1 = Button(c, text='+', command=self.add)
        self.b2=Button(c,text='-',command=self.sub)
        self.b3=Button(c,text='*',command=self.multi)
        self.b4= Button(c, text='/', command=self.div)
        self.b3.place(x=300,y=150)
        self.b4.place(x=400, y=150)
        self.b1.place(x=100,y=150)
        self.b2.place(x=200,y=150)
        self.l3.place(x=100,y=200)
        self.e3.place(x=200,y=200)
        self.l.place(x=170,y=5)
    def add(self):
        try:
            self.e3.delete(0, 'end')
            num1 = int(self.e1.get())
            num2 = int(self.e2.get())
            result = num1 + num2
            self.e3.insert(END, str(result))
        except ValueError:
            m.showwarning('ERROR','Please Enter a Valid Number..')



    def sub(self):
        try:
            self.e3.delete(0, 'end')
            num1 = int(self.e1.get())
            num2 = int(self.e2.get())
            result = num1 + num2
            self.e3.insert(END, str(result))
        except ValueError:
            m.showwarning('ERROR', 'Please Enter a Valid Number..')

    def multi(self):
        try:
            self.e3.delete(0, 'end')
            num1 = int(self.e1.get())
            num2 = int(self.e2.get())
            result = num1 * num2
            self.e3.insert(END, str(result))
        except ValueError:
            m.showwarning('ERROR', 'Please Enter a Valid Number..')


    def div(self):
        try:
            self.e3.delete(0, 'end')
            num1 = int(self.e1.get())
            num2 = int(self.e2.get())
            if num2!=0:
                result = num1 / num2
                self.e3.insert(END, str(result))
            else:
                m.showwarning('ERROR','Division by Zero is Not Allowed..')
        except ValueError:
            m.showwarning('ERROR', 'Please Enter a Valid Number..')

a=Tk()
s=file(a)
a.title('Calculator')
a.geometry('550x300')
a.resizable(False,False)
a.mainloop()

