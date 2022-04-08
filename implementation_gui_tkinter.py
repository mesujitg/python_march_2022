from classes import Triangle, Square, Circle, Rectangle

choice = int(input('Choose: 1. Triangle 2. Rectangle 3. Square 4. Circle '))
shapes = [['Triangle', 'Rectangle', 'Square', 'Circle'], [3, 4, 4, 0]]


def triangle():
    option = input('Calculate: 1. Area 2. Perimeter: ')
    t = Triangle(shapes[0][choice-1], shapes[1][choice-1])
    if option == '1':
        height = int(input('Enter Height of Triangle: ')) 
        base = int(input('Enter Length of Base of Triangle: '))
        t.set_height(height)
        t.set_base(base)
        print(t.show_info())
        print('Area: ', t.area())
    elif option == '2':
        side1 = float(input('Enter length of 1st side'))
        side2 = float(input('Enter length of 2nd side'))
        side3 = float(input('Enter length of 3rd side'))
        print(t.show_info())
        print('Perimeter', t.perimeter(side1, side2, side3))
    else:
        print('Invalid Selection')


def rectangle():
    pass


def square():
    option = input('Calculate: 1. Area 2. Perimeter: ')
    length = int(input('Enter length of Square: ')) 
    s = Square(shapes[0][choice-1], shapes[1][choice-1], length)
    print(s.show_info())
    if option == '1':
        print('Area: ', s.area())
    if option == '2':
        print('Perimeter: ', s.perimeter(length))

def circle():
    option = input('Calculate: 1. Area 2. Perimeter: ')
    radius = int(input('Enter Radius: ')) 
    c = Circle(shapes[0][choice-1], shapes[1][choice-1], radius)
    print(c.show_info())
    if option == '1':
        print('Area: ', c.area())
    if option == '2':
        print('Perimeter: ', c.perimeter())


if choice == 1:
    triangle()
elif choice == 2:
    rectangle()
elif choice == 3:
    square()
elif choice == 4:
    circle()
else:
    print('Invalid Selection')