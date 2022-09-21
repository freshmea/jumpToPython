if __name__ == '__main__':
    lineCount = {}
    # 파일 읽기
    with open("data.txt", 'r') as f:
        lineCnt = 1
        while True:
            line = f.readline()
            if not line:
                break
            # 내용 확인 및 딕셔너리 Count 추가
            for char in line:
                if char in "(),\"\n":
                    line = line.replace(char, '')

            for word in line.split():
                if word in lineCount:
                    lineCount[word].append(lineCnt)
                else:
                    lineCount[word] = [lineCnt]
            lineCnt += 1

    for v in lineCount.items():
        print(f"{v[0]} : {v[1]}")
