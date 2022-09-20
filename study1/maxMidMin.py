if __name__ =="__main__":
    a, b, c = input().split()

    if a > b:
        max = a
        min = b
    else:
        max = b
        min = a

    if c> max:
        mid = max
        max = c
    elif c > min:
        mid = c
    else:
        mid = min
        min = c


    print(f"max: {max}, mid: {mid}, min:{min}")