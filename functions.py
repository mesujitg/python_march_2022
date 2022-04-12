# function in python

# Non - Parameterized
def addNumbers():
    a = int(input('Enter first number'))
    b = int(input('Enter 2nd number'))
    print(a+b)


# Parameterized
def addNumbersP(a, b):
    return a+b

# num1 = input('Enter first number')
# print(num1.isalnum())

# num1 = int(input('Enter first number'))
# num2 = int(input('Enter 2nd number'))
print()
# result = addNumbersP(num1, num2)

# if result > 100:
#     print(result)

# def checkOddEven():
#     a = int(input('Enter a number'))
#     if a%2 == 0:
#         print('Given number is Even')
#     else:
#         print('Given number is Odd')

# checkOddEven()

# def checkOddEvenP(a):
#     if a%2 == 0:
#         print('Given number is Even')
#     else:
#         print('Given number is Odd')

# num = int(input('Enter a number'))
# checkOddEvenP(num)


import random

def wordgame(words):
    score = 0
    for i in words:
        w = list(i)
        random.shuffle(w)
        print(w)
        a = input('Enter: ')
        if a == i:
            score += 1
    return score

fruits = ['apple', 'orange', 'grapes', 'banana', 'pineapple']
result = wordgame(fruits)
print('Your Score is: ', result)