from math import pi

class User:
    name = ''
    gender = ''
    dob = ''
    nationality = ''
    address = ''
    email = ''
    phone = ''
    username = ''
    password = ''

    def login(self):
        pass



class Student(User):
    # name, gender, age, nationality, email, phone, course
    # visit, enroll, attain class/programs, upgrade, leave
    # CREATE INSERT/SAVE SELECT/RETRIEVAL UPDATE DELETE (CRUD)
    course = ''
    reg_id = ''

    def __init__(self):
        pass

    def setValues(self, name, gender, dob, nationality, email, phone, course, username, password):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.nationality = nationality
        self.email = email
        self.phone = phone
        self.course = course
        self.username = username
        self.password = password

    def addStudent(self, st):
        # st.append((self.name, self.gender))
        # list = []
        # list = [('ram', 'male'), (), ()]
        st.append({'name': self.name, 'gender': self.gender})
        # list = [{'name': 'ram', 'gender': 'male'}, {}, {}]

    def getStudents(self):
        pass

    def searchStudent(self):
        pass

    def updateStudent(self):
        pass

    def deleteStudent(self):
        pass


class Staff(User):
    type = ''
    shift = ''
    salary = ''

    def addStaff(self):
        pass

    def getStaff(self):
        pass

    def searchStaff(self):
        pass

    def updateStaff(self):
        pass

    def deleteStaff(self):
        pass


class Course:
    title = ''
    duration = ''
    format = ''
    fee = ''
    faculty = ''

# class Payment:
#     # student, date, amount, due
#     pass

# Ram male 25 nepali ram@email.com 9876543210 BBA [('2022-01-01', 20000), ('2022-03-01', 25000), ('2022-05-05', 40000)]



# Institute, Employee, Course, ClassRoom, Account

class Shape:
    name = ''
    no_of_side = ''

    def __init__(self, name, sides):
        self.name = name
        self.no_of_side = sides

    def show_info(self):
        return f'Shape: {self.name} \n No. of Sides: {self.no_of_side}'

    def perimeter(self, length):
        return self.no_of_side * length

    def area():
        pass


class Triangle(Shape):
    height = ''
    base = ''

    def __init__(self, name, sides, height, base):
        super().__init__(name, sides)
        self.height = height
        self.base = base

    def perimeter(self, a, b, c):
        return (a + b + c)

    def area(self):
        return ((self.base*self.height)/2)


class Rectangle(Shape):
    length = ''
    breadth = ''

    def __init__(self, name, sides, length, breadth):
        super().__init__(name, sides)
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return (2*(self.length + self.breadth))

    def area(self):
        return self.length * self.breadth


class Square(Shape):
    length = ''

    def __init__(self, name, sides, length):
        super().__init__(name, sides)
        self.length = length

    def area(self):
        return self.length**2

class Circle(Shape):
    radius = ''

    def __init__(self, name, sides, radius):
        super().__init__(name, sides)
        self.radius = radius

    def perimeter(self):
        return (2 * pi * self.radius)

    def area(self):
        return (pi*(self.radius**2))


t = Triangle('Triangle', 3, 10, 5)
r = Rectangle('Rectange', 4, 10, 5.55)
s = Square('Square', 4, 10)
c = Circle('Circle', 0, 14.55)

# print(t.area())
# print(r.area())
# print(r.area())
# print(s.area())
# print(c.area())

print(t.perimeter(10, 5, 7))
print(s.perimeter(10))

