def f(a):
    return a

def f():
    return 1

# def f(a = 1):
#     return a

if __name__ =='__main__':
    a = f()
    print(a)
    a = f(1)   # overloading 안됨.
    print(a)