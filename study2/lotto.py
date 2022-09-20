import random

if __name__ == '__main__':
    lotto = []
    while len(lotto) < 9:
        tmp = random.randint(1, 45)
        if tmp not in lotto:
            lotto.append(tmp)

    print(lotto)