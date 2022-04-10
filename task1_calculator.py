'''
Q. take two numbers and operation with user and 
show the result

a = 10
b = 20
op = *
Output:
-------
Result: 200
'''

# num1 = float(input('Enter first number: '))
# op = input('Choose: 1.+ 2.- 3.x 4./ : ')
# num2 = float(input('Enter second number: '))

# if op == '1':
#     print(num1+num2)
# elif op == '2':
#     print(num1-num2)
# elif op == '3':
#     print(num1*num2)
# elif op == '4':
#     print(num1/num2)
# else:
#     print('Invalid selection')
    


def calculate(num1, num2, op):
    if op == '1':
        return num1+num2
    elif op == '2':
        return num1-num2
    elif op == '3':
        return num1*num2
    elif op == '4':
        return num1/num2
    else:
        return 0
    
    

# num1 = float(input('Enter first number: '))
# op = input('Choose: 1.+ 2.- 3.x 4./ : ')
# num2 = float(input('Enter second number: '))
# print(calculate(num1, num2, op))


def calculate_np():
    try:
        num1 = float(input('Enter first number: '))
        op = input('Choose: 1.+ 2.- 3.x 4./ : ')
        num2 = float(input('Enter second number: '))
        result = 0
        if op == '1':
            result =  num1+num2
        elif op == '2':
            result = num1-num2
        elif op == '3':
            result = num1*num2
        elif op == '4':
            result = num1/num2
        else:
            result = 0
        print(result)
    except Exception as e:
        print(e, ': Enter Numeric value')
    finally:
        calculate_np()

calculate_np()



class Calculator:
    __operator = ''
    __first_num = ''
    __second_num = ''

    def __init__(self, op, fn, sn):
        self.__operator = op
        self.__first_num = fn
        self.__second_num = sn

    # def set_values(self, op, fn, sn):
    #     self.__operator = op
    #     self.__first_num = fn
    #     self.__second_num = sn

    def set_operator(self, op):
        # required validation
        self.__operator = op
    
    def set_first_num(self, fn):
        self.__first_num = fn

    def set_second_num(self, sn):
        self.__second_num = sn

    def get_operator(self):
        return self.__operator

    def calculate(self):
        result = 0
        if self.__operator == '+':
            result = self.__first_num + self.__second_num
        elif self.__operator == '-':
            result = self.__first_num - self.__second_num
        elif self.__operator == '*':
            result = self.__first_num * self.__second_num
        elif self.__operator == '/':
            result = self.__first_num / self.__second_num

        return result

    def cancel(self):
        pass



# num1 = input('Enter first number: ')
# op = input('Chose + or - or * or /: ')
# num2 = input('Enter second number: ')

# calc = Calculator(op, num1, num2, '+')
# calc.set_values(op, num1, num2)
# print(calc.__first_num, calc.__operator, calc.__second_num)
# print(calc.get_operator())


class Account:
    __name = ''
    __ac_no = ''
    __balance = ''

    def set_name(self, name):
        self.__name = name

    def set_acc(self, ac):
        self.__ac_no = ac

    def set_balance(self, balance):
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_acc(self):
        return self.__ac_no

    def get_balance(self):
        return self.__balance

    def __init__(self, n, ac, t, un, pw, bl):
        self.name = n
        self.ac_no = ac
        self.type = t
        self.username = un
        self.password = pw
        self.balance = bl

    def login(self):
        pass

    def transaction(self):
        pass

    def print_statement(self):
        pass

    def change_account_type(self):
        pass

    
