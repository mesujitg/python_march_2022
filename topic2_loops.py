# initialization, final_condition, increment

# n = int(input('Enter a number'))
# i = 1
# while i <= 10:
#     print(n, '*', i, '=', i*n)
#     i += 1

"""
Q. print multiplication (up to 10) of user given number.
5 * 1 = 5
5 * 2 = 10
..........
5*10 = 50

n = int(input('Enter a number'))
for i in range(1, 11):
    # print(n, '*', i, '=', i*n)
    print(f'{ n } * { i } = { i*n }')


i = 1
while i <= 10:
    print(n, '*', i, '=', i*n)
    i += 1
"""

"""
Q. Find factorial of a user given number.
5 = 1*2*3*4*5 OR 5*4*3*2*1
fact = 1
     = 1*2 [1*2]
     = 2*3 [1*2*3]
     = 6*4 [1*2*3*4]
     = 24*5 [1*2*3*4*5]
"""
# n = int(input('Enter a number'))
# fact = 1
# i = 2
# while i <= n:
#     fact = fact * i
#     i += 1
# print(fact)

"""
Q. State whether a user given number is prime of composite.
n = int(input('Enter a number'))
for i in range(2, n//2 + 1):
    if n%i == 0:
        print('Given number is composite')
        break
else:
    print('Given number is prime')

Q. Print Factors of a user given number.
n = int(input('Enter a number'))
for i in range(2, n//2 + 1):
    if n%i == 0:
        print(i)

Q. Print Multiples of user given number up to user given limit.

n = int(input('Enter a number'))
l = int(input('Enter a upper bound'))

# for i in range(1, l):
#     if (n*i <= l):
#         print(n*i)
#     else:
#         break

i = 1
while n*i <= l:
    print(n*i)
    i += 1

   
# for i in range(n, l+1, n):
#     print(i)

# i = n
# while i<=l:
#     print(i)
#     i += n

Q. Print Fibonacci series (any 10 or upto user given boundary).
0 1 1 2 3 5 8 13 21 34 

n = int(input('Enter a upper bound'))
a = 0
b = 1
print(a)
print(b)

while a+b <= n:
    c = a+b
    print(c)
    a = b
    b = c

# for i in range(8):
#     c = a+b
#     print(c)
#     a = b  # 1 1 
#     b = c  # 1 2
"""

'''
Q. 
1*1=1 1*2=2 ........ 1*10=10
2*1=2 2*2=4 ......... 2*10=20
............................
10*1=10 10*2=20 ....... 10*10=100

for i in range(6):
    for j in range(6):
        # print(i, 'x', j, '=', i*j, end=', ')
        print(f'{i} x {j} = {i*j}', end=', ')
    print()
'''

'''
*#*#*#      *           1               5 5 5 5 5       5 4 3 2 1
#*#*#*      **          1 2             4 4 4 4         5 4 3 2
*#*#*#      ***         1 2 3           3 3 3           5 4 3
#*#*#*      ****        1 2 3 4         2 2             5 4
*#*#*#      *****       1 2 3 4 5       1               5

1.
for i in range(6):
    for j in range(6):
        if (i+j)%2 == 0:
            print('*', end=' ')
        else:
            print('#', end=' ')
    print()
'''

for i in range(1,6):
    for j in range(5, i-1, -1):
        print(j, end=' ')
    print('')

'''
i=1
5 4 3 2 1
i=2
5 4 3 2
i=3
5 4 3
'''


for i in range(5, 0, -1):
    for j in range(i):
        print(5-j, end=' ')
    print('')

'''
i=5
5-0 5-1 5-2 5-3 5-4
i=4
5-0 5-1 5-2 5-3
'''

# for i in range (1,6):
#     for j in range (1,i+1):
#         print(f'*',end=' ')
#     print('')