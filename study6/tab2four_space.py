from sys import *

if __name__ == '__main__':
    srcFile = argv[1]
    desFile = argv[2]

    f = open(srcFile, 'r')
    str1 = f.read()
    f.close()

    result_str = str1.replace('\t', ' ' * 4)

    f = open(desFile, 'w')
    f.write(result_str)
    f.close()