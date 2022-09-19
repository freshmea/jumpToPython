# average.py

if __name__ == '__main__':
    print("input number of man  : ")
    man = int(input())
    print("input number of woman  : ")
    woman = int(input())
    manRatio = man / (man + woman) * 100
    womanRatio = woman / (man + woman) * 100

    print(f'manRatio : {manRatio:.2f} %  \t womanRatio : {womanRatio:.2f} %')
