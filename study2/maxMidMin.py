if __name__ =="__main__":
    number1 = int(input())
    number2 = int(input())
    number3 = int(input())
    midNumber = number1
    maxNumber = max(number1, number2, number3)
    minNumber = min(number1, number2, number3)
    if number1 == maxNumber:
        midNumber = number2
        if number2 == minNumber:
            midNumber = number3
    if number1 == minNumber:
        midNumber = number2
        if number2 == maxNumber:
            midNumber = number3

    print(f"max: {maxNumber}, mid: {midNumber}, min:{minNumber}")