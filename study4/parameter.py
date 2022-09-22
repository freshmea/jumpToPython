
g = 111

def flist(list1):
    list1[0] = 200
    list1 = [5, 6, 7, 8]

def f(a):
    a = 200

def f3():
    global g
    g = 222

if __name__ == '__main__':
    a = 100
    f(a)
    print(a)

    list1 = [100]
    flist(list1)
    print(list1)

    f3()
    print(g)
    list4=[[1,2,3],[4,5,6],[7,8,9]]
    print(list4[1][0])