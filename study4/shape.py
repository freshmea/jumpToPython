from abc import *

class Shape(metaclass=ABCMeta):
    classtype1 = 'Shape'
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def move(self, x, y ):
        self.__x += x
        self.__y += y

    @abstractmethod
    def area(self):
        pass

    @staticmethod
    def typeid1():
        return Shape.classtype1

class Rectangle(Shape):
    __classtype = 'Rectangle'
    def __init__(self, x=0, y=0, width=0, height=0):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    @classmethod
    def typeid(cls):
        return cls.__classtype

class Circle(Shape):
    __classtype = 'Circle'
    def __init__(self, x=0, y=0, radius=0):
        super().__init__(x, y)
        self.__radius = radius

    def area(self):
        return 3.141592 * self.__radius * self.__radius

    def radius(self):
        return self.__radius

    @classmethod
    def typeid(cls):
        return cls.__classtype, Shape.classtype1

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

    for s in shapes:
        print_area(s)

    # print_shapes(shapes)
    print_shapes2(shapes)