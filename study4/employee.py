
class Employee:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name

if __name__ == '__main__':
    a = Employee(100, 'choi')
    print(a.getId(), " : ", a.getName())
    # print(a.__id, " : ", a.__name) private 접근 에러.
