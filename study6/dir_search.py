import os

def searchDir(path):
    filenames = os.listdir(path)
    for filename in filenames:
        if os.path.isdir(filename):
            print( ' ??', filename)
            searchDir(filename)
        else:
            result = os.path.splitext(filename)[-1]
            if result == '.py':
                print(filename)


if __name__ == '__main__':
    searchDir('/home/aa/PycharmProjects/jumpToPython/study5')
