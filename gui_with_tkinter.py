# import tkinter as tk
from cgitb import text
from msilib.schema import RadioButton
from tkinter import BOTTOM, LEFT, RIGHT, TOP, Button, Entry, Frame, StringVar, IntVar, ttk, Tk, Label, Text

'''
label, textbox, multiline textbox, button, radio, dropdown, checkbox
frame
grid(), pack(), place()
'''
users = [
            {'name':'Ram', 'username':'ram123', 'password':'12345', 'balance': 50000.00},
            {'name':'Shyam', 'username':'shyam', 'password':'54321', 'balance': 25000.00},
            {'name':'Hari', 'username':'hari', 'password':'11111', 'balance': 100000.00},
        ]

root = Tk()
root.geometry('250x200')
root.title('User Login')
root.resizable(False, False)

choice = StringVar()
amount = IntVar()
balance = 0

def on_login_click():
    global balance
    un = entry_un.get()
    pw = entry_pw.get()
    for i in users:
        if un == i['username']:
            if pw == i['password']:
                root.destroy()
                root_db = Tk()
                # root_db.geometry('500x500')
                root_db.title('User Login')
                root_db.resizable(False, False)

                balance = i["name"]

                label_info = Label(root_db, text=f'Welcome: {i["name"]}! Yor balance is: {i["balance"]}')
                label_info.grid(row=0, column=0, columnspan=2)

                # print('Welcome: ', i['name'])
                # print('Yor balance is: ', i['balance'])

                # choice = input('Enter D for Deposite / W for Withdrawal')
                # amount = float(input('Enter amount'))
                radio_dep = ttk.Radiobutton(root_db, text='Deposite')
                radio_dep.grid(row=1, column=0)
                radio_wd = ttk.Radiobutton(root_db, text='Withdraw')
                radio_wd.grid(row=1, column=1)

                label_am = Label(root_db, text="Amount", textvariable=amount)
                label_am.grid(row=2, column=0)

                entry_am = Entry(root_db)
                entry_am.grid(row=2, column=1)

                btn_proceed = Button(root_db, text='Proceed')
                btn_proceed.grid(row=3, column=0, columnspan=2)

                # if choice == 'D' or choice == 'd':
                #     # print('Yor balance is: ', i['balance']+amount)
                #     i['balance'] = i['balance']+amount
                # elif choice == 'W' or choice == 'w':
                #     # print('Yor balance is: ', i['balance']+amount)
                #     i['balance'] = i['balance']-amount
                # print('Yor balance is: ', i['balance'])
            else:
                # print('Wrong credentials')
                label_show.config(text='Wrong credentials')
            break
        else:
            # print('Doesnot exist')
            label_show.config(text='Doesnot exist')

def on_proceed_click():
    if choice == 'D' or choice == 'd':
        i['balance'] = i['balance']+amount
    elif choice == 'W' or choice == 'w':
        i['balance'] = i['balance']-amount

# grid, place, pack
label_un = Label(root, text='Username', padx=10, pady=10)
label_un.grid(row=0, column=0)

entry_un = Entry(root)
entry_un.grid(row=0, column=1)

label_pw = Label(root, text='Password', padx=10, pady=10)
label_pw.grid(row=1, column=0)

entry_pw = Entry(root, show='*')
entry_pw.grid(row=1, column=1)

btn_login = Button(root, text='Login', padx=10, pady=10, height=1, 
                    width=15, command=on_login_click)
btn_login.grid(row=2, column=0, columnspan=2)

label_show = Label(root)
label_show.grid(row=3, column=0, columnspan=2)

# my_frame = Frame(root, padx=10, pady=10, background='red')
# my_frame.grid(row=3, column=0,  columnspan=2)

# tb_comment = Text(my_frame, height=4, width=8, pady=10)
# tb_comment.pack(side=LEFT)

# btn_comment = Button(my_frame, text='Comment')
# btn_comment.pack(side=RIGHT)

root.mainloop()