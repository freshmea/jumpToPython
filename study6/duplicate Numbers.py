import re

def duplicate_number(data):
    p = re.compile('[0-9]')
    original = set()
    if len(str(data)) != 10: return False
    for i in range(0, 10):
        original.add(str(i))
    test = set()
    for i in p.finditer(str(data)):
        test.add(i.group())
    if original == test:
        return True
    return False

if __name__ == '__main__':
    print(duplicate_number(1234567890))
    print(duplicate_number(12345678900))
    print(duplicate_number(12890))
    print(duplicate_number(1029384756))
    print(duplicate_number('aaa1029384756'))
    print(duplicate_number('ddd'))
