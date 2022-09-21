def fsum(list1):
    sumv = 0
    for i in list1:
        sumv += i
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

if __name__ == '__main__':

    list1 = [abs(i-50) for i in range(100)]
    print(fsum(list1))
    print(len(list1))
    print(ffind(list1 , 27))
