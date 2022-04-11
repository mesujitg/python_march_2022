# import tkinter as tk
from tkinter import Button, Entry, Frame, ttk, Tk, Label, Text

'''
label, textbox, multiline textbox, button, radio, dropdown, checkbox
'''

root = Tk()
root.geometry('500x500')
root.title('User Login')
root.resizable(False, False)

# grid, place, pack
label_un = Label(root, text='Username', padx=10, pady=10)
label_un.grid(row=0, column=0)

entry_un = Entry(root)
entry_un.grid(row=0, column=1)

label_pw = Label(root, text='Password', padx=10, pady=10)
label_pw.grid(row=1, column=0)

entry_pw = Entry(root)
entry_pw.grid(row=1, column=1)

btn_login = Button(root, text='Login', padx=10, pady=10, height=1, width=15)
btn_login.grid(row=2, column=0, columnspan=2)

my_frame = Frame(root, padx=10, pady=10, background='red')
my_frame.grid(row=3, column=0,  columnspan=2)

tb_comment = Text(my_frame, height=4, width=8, pady=10)
tb_comment.grid(row=0, column=0)

btn_comment = Button(my_frame, text='Comment')
btn_comment.grid(row=1, column=0)

root.mainloop()