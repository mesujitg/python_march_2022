from classes import Shape, Triangle, Square, Circle, Rectangle

choice = int(input('Choose: 1. Triangle 2. Rectangle 3. Square 4. Circle '))

# shapes = [{'Triangle': 3}, {'Rectangle': 4}, {'Square': 4}, 
#             {'Circle': 0}]
shapes = [['Triangle', 'Rectangle', 'Square', 'Circle'], [3, 4, 4, 0]]

# shape = Shape('name', no_of_side)
shape = Shape(shapes[0][choice-1], shapes[1][choice-1])
print(shape.show_info())

