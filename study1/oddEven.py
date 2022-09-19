# oddEven.py

if __name__ == '__main__':
    num = int(input())
    # print(f"{num} is a odd number.") if (num % 2) == 1 else print(f"{num} is a even number.")
    print(f"{num} is a odd number.") if num % 2 else print(f"{num} is a even number.")
