if __name__ =="__main__":

    grades = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']
    score = int(input())
    print(grades[0])
    grade = grades[score // 10]
    print(f'score :{score} --- {grade}')