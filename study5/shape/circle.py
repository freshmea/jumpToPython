from shape import Shape

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

