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

    def area():
        pass


class Triangle(Shape):
     def perimeter(self):
         pass


class Rectangle(Shape):
    @staticmethod
    def area(length, bradth):
        return length * bradth


class Square(Shape):
    @staticmethod
    def area(length):
        return length**2


t = Triangle()
r = Rectangle()
s = Square()
print(t.area(10, 5))
print(r.area(10, 5))
print(s.area(10))

# Animal
# Dog
# Cat
# Crocodile