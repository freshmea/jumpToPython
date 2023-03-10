from shape import Shape

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