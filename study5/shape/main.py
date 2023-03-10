# from shape import *

import pickle
from rectangle import Rectangle
from circle import Circle

def print_area(shape):
    print(f"area : {shape.area():.2f}")

def print_shapes(shapes):
    for shape in shapes:
        if type(shape) == Rectangle:
            print(f"this is Rectangle width :{shape.width()} height : {shape.height()}")
        if type(shape) == Circle:
            print(f"this is Circle radius : {shape.radius()}")

def print_shapes2(shapes):
    for shape in shapes:
        print(shape.typeid1(), shape.typeid())
        if shape.typeid() == 'Rectangle':
            print(f"this is Rectangle width :{shape.width()} height : {shape.height()}")
        if shape.typeid() == 'Circle':
            print(f"this is Circle radius : {shape.radius()}")

def print_shapes3(shapes):
    for shape in shapes:
        if isinstance(shape, Rectangle):
            print(f"this is Rectangle width :{shape.width()} height : {shape.height()}")
        if isinstance(shape, Circle):
            print(f"this is Circle radius : {shape.radius()}")

if __name__ == '__main__':
    r = Rectangle(10, 10, 20, 40)
    print(r.area())
    c = Circle(10, 100, 8)
    print(c.area())
    # s = Shape(1, 1)  추상 클래스 선언으로 에러 발생
    shapes = []
    shapes.append(Rectangle(10, 10, 100, 50))
    shapes.append(Rectangle(0, 0, 50, 10))
    shapes.append(Circle(0, 0, 5))
    shapes.append(Circle(100, 100, 10))
    shapes.append(Rectangle(50, 50, 5, 5))

    f = open("pickle_data.dat", 'wb')
    pickle.dump(shapes, f)  # 객체를 그대로 저장하고 불러올 수 있다.
    f.close()

    f = open('pickle_data.dat', 'rb')
    data = pickle.load(f)
    print(data)
    print_shapes3(data)


    for s in shapes:
        print_area(s)

    # print_shapes(shapes)
    print_shapes3(shapes)