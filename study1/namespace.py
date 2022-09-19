if __name__ == "__main__":
    class abc(object):
        a = 10
        print(locals())
        print(dir())

    aaa = abc()
    print(locals())
    print(dir())
    print(abc.__dict__)
    print(aaa.__dict__)
