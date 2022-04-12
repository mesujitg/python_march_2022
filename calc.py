from tkinter import *

root = Tk()
root.geometry('200x200')
root.title('Calculator')

# first row
display = Entry(root)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# second row
btn7 = Button(root, text='7', width=2, height=1)
btn7.grid(row=1, column=0)

btn8 = Button(root, text='8', width=2, height=1)
btn8.grid(row=1, column=1)

btn9 = Button(root, text='9', width=2, height=1)
btn9.grid(row=1, column=2)

btndiv = Button(root, text='/', width=2, height=1)
btndiv.grid(row=1, column=3)

# third row
btn4 = Button(root, text='4', width=2, height=1)
btn4.grid(row=2, column=0)

btn5 = Button(root, text='5', width=2, height=1)
btn5.grid(row=2, column=1)

btn6 = Button(root, text='6', width=2, height=1)
btn6.grid(row=2, column=2)

btnmul = Button(root, text='x', width=2, height=1)
btnmul.grid(row=2, column=3)

root.mainloop()