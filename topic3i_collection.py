
users = [
            {'name':'Ram', 'username':'ram123', 'password':'12345', 'balance': 50000.00},
            {'name':'Shyam', 'username':'shyam', 'password':'54321', 'balance': 25000.00},
            {'name':'Hari', 'username':'hari', 'password':'11111', 'balance': 100000.00},
        ]

un = input('Enter username: ')
pw = input('Enter password: ')

# Q. check if the given username exist? Check if password is correct?
for i in users:
    if un == i['username']:
        if pw == i['password']:
            print('Welcome: ', i['name'])
            print('Yor balance is: ', i['balance'])
            choice = input('Enter D for Deposite / W for Withdrawal')
            amount = float(input('Enter amount'))
            if choice == 'D' or choice == 'd':
                # print('Yor balance is: ', i['balance']+amount)
                i['balance'] = i['balance']+amount
            elif choice == 'W' or choice == 'w':
                # print('Yor balance is: ', i['balance']+amount)
                i['balance'] = i['balance']-amount
            print('Yor balance is: ', i['balance'])
        else:
            print('Wrong credentials')
        break
else:
    print('Doesnot exist')




