import pandas

students = ['ram', 'shyam', 'hari', 'krishna']
student = {'name': 'ram', 'course': 'django', 'mobile': 9812345678}

print(pandas.Series(students))
print(pandas.Series(student))


students_multi = {
            'name':['Ram', 'Shyam', 'Hari'], 
            'course':['django', 'data science', 'AI'], 
            'mobile':[9812345678, 9876543211, 9845678314]
            }

print(pandas.DataFrame(students_multi))

file = pandas.read_csv('subjects.csv')
print(file)

file = pandas.read_json('subjects.json')
print(file)



