if __name__ == '__main__':
    grades = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']
    gradeCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    print(type(gradeCount))

    scores = [95, 83, 100, 75, 69, 60, 84, 95, 30, 40]

    for score in scores:
        gradeCount[grades[score//10]] += 1
    print(gradeCount)
