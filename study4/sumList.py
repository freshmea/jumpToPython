def fsum(list1):
    sumv = 0
    for i in list1:
        sumv += i
    list1[0] = 100
    return sumv

def ffind(list1, v):
    re = []
    for i, x in enumerate(list1):
        if v == x:
            print( f'{v} is found! index : {i}')
            re.append(i)
            continue
        if i == len(list1)-1 and len(re)==0:
            print(f'{v} is not found!')
    return re

def findValueList(list1, value):
    i = 0
    while i != len(list1):
        if value == list1[i]:
            break
        i += 1
    if i ==len(list1):
        return -1
    else:
        return i

def isFoundValue(list1, value):
    return  value in list1

if __name__ == '__main__':

    list1 = [abs(i-50) for i in range(100)]
    print(fsum(list1))
    print(len(list1))
    print(ffind(list1 , 27))
    print(list1[0])

    if isFoundValue(list1, 0):
        print("0 is in list")
    else:
        print('o is not in list')
    index = findValueList(list1, 30)
    print("index : ", index)
