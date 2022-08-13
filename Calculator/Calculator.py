import tkinter
from tkinter import *
from tkinter import messagebox

rootWindow=tkinter.Tk()

num1=0
operator=""
val=""

def btn1Pressed():
    global val
    val=val+'1'
    Data.set(val)
def btn2Pressed():
    global val
    val=val+"2"
    Data.set(val)
def btn3Pressed():
    global val
    val=val+'3'
    Data.set(val)
def btn4Pressed():
    global val
    val=val+'4'
    Data.set(val)
def btn5Pressed():
    global val
    val=val+'5'
    Data.set(val)
def btn6Pressed():
    global val
    val=val+'6'
    Data.set(val)
def btn7Pressed():
    global val
    val=val+'7'
    Data.set(val)
def btn8Pressed():
    global val
    val=val+'8'
    Data.set(val)
def btn9Pressed():
    global val
    val=val+'9'
    Data.set(val)
def btn0Pressed():
    global val
    val=val+'0'
    Data.set(val)
def btnPlusPressed():
    global operator
    global num1
    global val
    operator = "+"
    num1=int(val)
    val=val+"+"
    Data.set(val)
def btnMinsPressed():
    global operator
    global num1
    global val
    operator = "-"
    if val=='':
        val=val+'-'
        if val=="-":
            num1=0
        else:
            num1=int(val)
    else:
        num1=int(val)
        val=val+"-"
    
    Data.set(val)
def btnMlyPressed():
    global operator
    global num1
    global val
    operator = "*"
    num1=int(val)
    val=val+"*"
    Data.set(val)
def btnDivPressed():
    global operator
    global num1
    global val
    operator = "/"
    num1=int(val)
    val=val+"/"
    Data.set(val)
def btnEqualPressed():
    global val
    global num1
    global operator
    temp=val
    num2=int((temp.split(operator)[1]))
    if operator=="+":
        result=num1+num2
        val=str(result)
        Data.set(result)
    elif operator=="-":
        result=num1-num2
        val=str(result)
        Data.set(result)
    elif operator=="*":
        result=num1*num2
        val=str(result)
        Data.set(result)
    elif operator=="/":
        if num2==0:
            messagebox.showerror("Error","Division by zero is not allowed.")
            val=""
            num1=0
            operator=""
            Data.set(val)
        else:
            result=num1/num2
            val=str(result)
            Data.set(result)
def btnCPressed():
    global val
    global num1
    global operator
    val=""
    num1=0
    operator=""
    Data.set(val)





rootWindow.geometry("250x400+450+200")
rootWindow.title('Claculator')
rootWindow.resizable(0,0)

Data=StringVar()


lbl=Label(rootWindow,textvariable=Data,anchor=SE,bg='#D3D3D3',font=('Verdana',22))
lbl.pack(expand=True,fill='both')

btnrow1=Frame(rootWindow)
btnrow1.pack(expand=True,fill='both')
btnrow2=Frame(rootWindow)
btnrow2.pack(expand=True,fill='both')
btnrow3=Frame(rootWindow)
btnrow3.pack(expand=True,fill='both')
btnrow4=Frame(rootWindow)
btnrow4.pack(expand=True,fill='both')


btn1=Button()
btn2=Button()
btn3=Button()
btnPlus=Button()
btn4=Button()
btn5=Button()
btn6=Button()
btnMins=Button()
btn7=Button()
btn8=Button()
btn9=Button()
btnMly=Button()
btnC=Button()
btn0=Button()
btnEqual=Button()
btnDiv=Button()


def button(btn1,frame,txt,cmd):
    btn1=Button(
    frame,
    text=txt,
    font=("Verdana",22),
    relief=GROOVE,
    border=False,
    command=cmd
    )
    btn1.pack(side=LEFT,expand=True,fill='both')

button(btn1,btnrow1,'1',btn1Pressed)
button(btn2,btnrow1,'2',btn2Pressed)
button(btn3,btnrow1,'3',btn3Pressed)
button(btnPlus,btnrow1,'+',btnPlusPressed)
button(btn4,btnrow2,'4',btn4Pressed)
button(btn5,btnrow2,'5',btn5Pressed)
button(btn6,btnrow2,'6',btn6Pressed)
button(btnMins,btnrow2,'-',btnMinsPressed)
button(btn7,btnrow3,'7',btn7Pressed)
button(btn8,btnrow3,'8',btn8Pressed)
button(btn9,btnrow3,'9',btn9Pressed)
button(btnMly,btnrow3,'*',btnMlyPressed)
button(btnC,btnrow4,'C',btnCPressed)
button(btn0,btnrow4,'0',btn0Pressed)
button(btnEqual,btnrow4,'=',btnEqualPressed)
button(btnDiv,btnrow4,'/',btnDivPressed)

rootWindow.mainloop()

