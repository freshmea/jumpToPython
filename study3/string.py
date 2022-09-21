if __name__ == "__main__":
    str = 'knicing on the heaven\'s door'
    print(str)

    list1 = str.split()
    print(list1)

    str = '1 9 3'
    list2 = [int(s) for s in str.split()]

    list3=[]
    for s in list2:
        list3.append(int(s))