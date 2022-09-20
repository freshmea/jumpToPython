import random

def shuffle(list):
    for _ in range(0, 10000):
        i = random.randint(0,len(list)-1)
        j = random.randint(0,len(list)-1)
        tmp = list[i]
        list[i] = list[j]
        list[j] = tmp

if __name__ == '__main__':
    list1 = [1, 2, 3, 4 ,5]
    list2 = [1, 2.2, 'abcd', True, list1]

    print(list1, end='\t')
    print(list2)

    for item in list2:
        print(item, end = '\t')
    print('')
    list3=[i for i in range(10)]
    print(list3)
    list4=[random.randint(1, 9) for _ in range(0,3)]
    print(list4)
    print(list4)
    shuffle(list1)
    print(list1)

