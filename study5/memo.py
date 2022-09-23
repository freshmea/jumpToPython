import sys
option = sys.argv[1]

if option == '-a':
    f = open('memo.txt', 'a')
    memo = sys.argv[2]
    f.write(memo)
    f.write('\n')
    f.close()
