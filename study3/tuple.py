def func(*arg):
    av = 100
    bv = 200
    for v in arg:
        av += v
    return av, bv


if __name__ == "__main__":
    list1 = func(1, 2, 3)   # packing
    print(list1)
    print(*list1)           # unpacking
    print(type(func()))
