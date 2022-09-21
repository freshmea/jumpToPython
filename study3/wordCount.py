from typing import Dict

if __name__ == '__main__':
    wordCount: Dict[str, int] = {}
    # 파일 읽기
    with open("data.txt", 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break

            # 내용 확인 및 딕셔너리 Count 추가
            for word in line.split():
                if word in wordCount:
                    wordCount[word] += 1
                else:
                    wordCount[word] = 1

    print(wordCount)
    print(len(wordCount))

    # maxS = max(wordCount.items(),key=lambda x: x[1])

    def func(da):
        return da[1]
    maxS = max(wordCount.items(), key=func)
    print(maxS)


