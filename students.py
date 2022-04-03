from classes import Student
student_list = []

def addSt():
    name = input('Enter your name: ')
    gender = input('Gender: m/f/o')
    dob = input('Enter your date of birth: ')
    nationality = input('Enter your date of nationality: ')
    email = input('Enter your email: ')
    phone = input('Enter your mobile: ')
    course = input('Enter your Course: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    st = Student()
    st.setValues(name, gender, dob, nationality, email, phone, course, username, password)
    st.addStudent(student_list)

    print(student_list)
    addSt()

addSt()
