from ctypes import alignment
from tkinter import *

root = Tk()
root.geometry('200x200')
root.title('Calculator')

num1 = 0
num2 = 0
op = ''

def on_btn_click(val):
    global num1, num2, op
    if val == 'c':
        display.delete(0, END)

    elif val == '+' or val == '-' or val == '*' or val == '/':
        op = val
        num1 = float(display.get())
        display.delete(0, END)

    elif val == '=':
        num2 = float(display.get())
        display.delete(0, END)
        
        if  op == '+':
            result = num1 + num2
        elif  op == '-':
            result = num1 - num2
        elif  op == '*':
            result = num1 * num2
        elif  op == '/':
            result = num1 / num2

        display.insert(0, result)

    else:    
        display.insert(END, val)

# first row
display = Entry(root, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# second row
btn7 = Button(root, text='7', width=2, height=1, command=lambda val=7: on_btn_click(val))
btn7.grid(row=1, column=0)

btn8 = Button(root, text='8', width=2, height=1, command=lambda val=8: on_btn_click(val))
btn8.grid(row=1, column=1)

btn9 = Button(root, text='9', width=2, height=1, command=lambda val=9: on_btn_click(val))
btn9.grid(row=1, column=2)

btndiv = Button(root, text='/', width=2, height=1, command=lambda val='/': on_btn_click(val))
btndiv.grid(row=1, column=3)

# third row
btn4 = Button(root, text='4', width=2, height=1, command=lambda val=4: on_btn_click(val))
btn4.grid(row=2, column=0)

btn5 = Button(root, text='5', width=2, height=1, command=lambda val=5: on_btn_click(val))
btn5.grid(row=2, column=1)

btn6 = Button(root, text='6', width=2, height=1, command=lambda val=6: on_btn_click(val))
btn6.grid(row=2, column=2)

btnmul = Button(root, text='x', width=2, height=1, command=lambda val='*': on_btn_click(val))
btnmul.grid(row=2, column=3)

# fourth row
btn1 = Button(root, text='1', width=2, height=1, command=lambda val=1: on_btn_click(val))
btn1.grid(row=3, column=0)

btn2 = Button(root, text='2', width=2, height=1, command=lambda val=2: on_btn_click(val))
btn2.grid(row=3, column=1)

btn3 = Button(root, text='3', width=2, height=1, command=lambda val=3: on_btn_click(val))
btn3.grid(row=3, column=2)

btnsub = Button(root, text='-', width=2, height=1, command=lambda val='-': on_btn_click(val))
btnsub.grid(row=3, column=3)

# fifth row
btnc = Button(root, text='C', width=2, height=1, command=lambda val='c': on_btn_click(val))
btnc.grid(row=4, column=0)

btn0 = Button(root, text='0', width=2, height=1, command=lambda val=0: on_btn_click(val))
btn0.grid(row=4, column=1)

btneq = Button(root, text='=', width=2, height=1, command=lambda val='=': on_btn_click(val))
btneq.grid(row=4, column=2)

btnadd = Button(root, text='+', width=2, height=1, command=lambda val='+': on_btn_click(val))
btnadd.grid(row=4, column=3)

root.mainloop()