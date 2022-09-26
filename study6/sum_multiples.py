
if __name__ == '__main__':
    sum = 0
    i = 1
    list1 = []
    while i < 1000:
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            list1.append(i)
        i += 1

    print('sum : ', sum)

    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i% 5 == 0:
            sum += i

    print('sum : ', sum)