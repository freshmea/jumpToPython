
if __name__ == '__main__'   :
    f = open("data.txt", 'r')
    data = f.read()
    data = data.split()
    list = list(data)
    dict = { }

    for i in list :
        dict[i] = 0

    for i in list :
        dict[i] += 1

    print(dict)