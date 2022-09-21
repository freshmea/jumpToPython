
if __name__ == "__main__":
    list1 =[i+1 for i in range(10) if i%2==1]
    list2 = [1 if 4%2==1 else 0]
    print(list1)
    print(list2)

    for v in list1:
        print(v)

    print(list1[0:5])
    print(list1[:2])
    print(list1[::-1])

    list2=[list1[i] for i in range(-1, -6, -1)]
    print(list2)