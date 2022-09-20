import random

if __name__ == '__main__':
    # 정답 생성
    question = []
    while len(question) < 3:
        tmp = random.randint(1, 9)
        if tmp not in question:
            question.append(tmp)

    count = 1
    print(question)
    while True:
        strike = ball = 0

        # 입력값
        print('Input Number (a, b, c):')
        a, b, c = input().split()
        answer = [int(a), int(b), int(c)]

        #입력값 확인
        for i in question:
            if i in answer:
                if question.index(i) == answer.index(i):
                    strike += 1
                else:
                    ball += 1

        print(f'Strike : {strike} Ball : {ball}')
        if strike == 3:
            break
        count += 1

    print(f'Congratulation! your count : {count}')
