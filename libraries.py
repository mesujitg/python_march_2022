# libraries
import math as m
# from math import sqrt
# from datetime import datetime
import datetime
import random
import re

# print(sqrt(64))
# print(m.sqrt(64))
# print(m.ceil(6.00001))
# print(m.floor(6.99999))

# print(datetime.datetime.now())

# fruits = ['apple', 'orange', 'grapes', 'banana', 'pineapple']
# word = list(fruits[0])
# random.shuffle(word)
# print(word)

name = input('Enter your name: ')
dob = input('Enter your date of birth: ')
email = input('Enter your email: ')
phone = input('Enter your mobile: ')
username = input('Enter your username: ')
password = input('Enter your password: ')

regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_phone = r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}'


def validate():
    msg = ''
    if not name.isalpha():
        msg += 'Invalid Name \n'
    if not username.isalnum():
        msg += 'Invalid Username \n'
    if not re.fullmatch(regex_email, email):
        msg += 'Invalid Email \n'
    if not re.fullmatch(regex_phone, phone):
        msg += 'Invalid Phone \n'

    return msg

if validate() == '':
    print('Name: ', name)
    print('DoB: ', dob)
    print('Email: ', email)
    print('Phone: ', phone)
    print('Username: ', username)
else:
    print(validate())
