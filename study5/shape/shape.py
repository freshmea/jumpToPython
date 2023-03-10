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


