from ctypes import alignment
from tkinter import *

root = Tk()
# root.geometry('250x280')
root.title('Calculator')

num1 = 0
num2 = 0
op = ''

def on_btn_click(val):
    global num1, num2, op
    if val == 'c':
        display.delete(0, END)

    elif val == 'back':
        display.delete(len(display.get())-1, END)

    elif val == '+' or val == '-' or val == '*' or val == '/':
        op = val
        num1 = float(display.get())
        display.delete(0, END)

    elif val == '=':
        num2 = float(display.get())
        display.delete(0, END)
        # result = 0
        
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


calc_frame = Frame(root, padx=20, pady=10)
calc_frame.grid(row=0, column=0)

# first row
display = Entry(calc_frame, justify=RIGHT, font=('Georgia 20'), width=10)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# second row
btn7 = Button(calc_frame, text='7', width=4, height=2, command=lambda val=7: on_btn_click(val))
btn7.grid(row=1, column=0)

btn8 = Button(calc_frame, text='8', width=4, height=2, command=lambda val=8: on_btn_click(val))
btn8.grid(row=1, column=1)

btn9 = Button(calc_frame, text='9', width=4, height=2, command=lambda val=9: on_btn_click(val))
btn9.grid(row=1, column=2)

btndiv = Button(calc_frame, text='/', width=4, height=2, command=lambda val='/': on_btn_click(val))
btndiv.grid(row=1, column=3)

# third row
btn4 = Button(calc_frame, text='4', width=4, height=2, command=lambda val=4: on_btn_click(val))
btn4.grid(row=2, column=0)

btn5 = Button(calc_frame, text='5', width=4, height=2, command=lambda val=5: on_btn_click(val))
btn5.grid(row=2, column=1)

btn6 = Button(calc_frame, text='6', width=4, height=2, command=lambda val=6: on_btn_click(val))
btn6.grid(row=2, column=2)

btnmul = Button(calc_frame, text='x', width=4, height=2, command=lambda val='*': on_btn_click(val))
btnmul.grid(row=2, column=3)

# fourth row
btn1 = Button(calc_frame, text='1', width=4, height=2, command=lambda val=1: on_btn_click(val))
btn1.grid(row=3, column=0)

btn2 = Button(calc_frame, text='2', width=4, height=2, command=lambda val=2: on_btn_click(val))
btn2.grid(row=3, column=1)

btn3 = Button(calc_frame, text='3', width=4, height=2, command=lambda val=3: on_btn_click(val))
btn3.grid(row=3, column=2)

btnsub = Button(calc_frame, text='-', width=4, height=2, command=lambda val='-': on_btn_click(val))
btnsub.grid(row=3, column=3)

# fifth row
btnc = Button(calc_frame, text='C', width=4, height=2, command=lambda val='c': on_btn_click(val))
btnc.grid(row=4, column=0)

btn0 = Button(calc_frame, text='0', width=4, height=2, command=lambda val=0: on_btn_click(val))
btn0.grid(row=4, column=1)

btneq = Button(calc_frame, text='=', width=4, height=2, command=lambda val='=': on_btn_click(val))
btneq.grid(row=4, column=2)

btnadd = Button(calc_frame, text='+', width=4, height=2, command=lambda val='+': on_btn_click(val))
btnadd.grid(row=4, column=3)

# sixth row
btnc = Button(calc_frame, text='<=', width=4, height=2, command=lambda val='back': on_btn_click(val))
btnc.grid(row=5, column=0)

btn0 = Button(calc_frame, text='.', width=4, height=2, command=lambda val='.': on_btn_click(val))
btn0.grid(row=5, column=1)

btneq = Button(calc_frame, text='^', width=4, height=2, command=lambda val='=': on_btn_click(val))
btneq.grid(row=5, column=2)

btnadd = Button(calc_frame, text='%', width=4, height=2, command=lambda val='%': on_btn_click(val))
btnadd.grid(row=5, column=3)

root.mainloop()