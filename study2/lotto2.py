import random

def shuffle(list):
    i = random.randint(0,len(list)-1)
    j = random.randint(0,len(list)-1)
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

if __name__ == '__main__':
    list1 = [i for i in range(1,46)]
    for _ in range(1, 1000000):
        shuffle(list1)
    # print(list1)
    print(list1[:7])
