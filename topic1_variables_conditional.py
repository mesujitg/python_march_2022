# name = "Ram"
# age = 25
# income = 50000.00
# is_married = False

# print('Name: ', name)
# print('Age: ', age)

# add two user given numbers
# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter 2nd number: '))
# print(num1+num2)
# print(int(num1)+int(num2))

"""
num1 = int(input('Enter a number: '))

if num1 == 1:
    print('Sunday')
elif num1 == 2:
    print('Monday')
elif num1 == 3:
    print('Tuesday')
elif num1 == 4:
    print('Wednesday')
elif num1 == 5:
    print('Thursday')
elif num1 == 6:
    print('Friday')
elif num1 == 7:
    print('Saturday')
else:
    print('Invalid')
"""

# a program to check whether a user given number is odd or even.
try:
    num = int(input('Enter a number: '))
    if num%2 == 0:
        print('Even')
    else:
        print('Odd')
except Exception as e:
    print(e, ': Please enter numeric value') 
finally:
    print('ok')

    