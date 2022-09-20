import random

if __name__ == "__main__":
    question = []
    while len(question) < 3:
        tmp = random.randint(0, 10)
        if tmp not in question:
            question.append(tmp)

    count = 1
    print(question)
    while True:
        strike = 0
        ball = 0
        print('Input Number (a, b, c):')
        a, b, c = input().split()
        answer = [int(a), int(b), int(c)]

        for i in question:
            if i in answer:
                if question.index(i) == answer.index(i):
                    strike += 1
                else:
                    ball += 1

        print(f'Strke : {strike} Ball : {ball}')
        if strike == 3:
            break
        count += 1

    print(f'Congraturation! your count : {count}')
