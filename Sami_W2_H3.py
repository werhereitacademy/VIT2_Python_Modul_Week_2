if __name__ == '__main__':
    Students = []
    Scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
    Students.append((name, score))                                 #Bu ne ise yaradi
    Scores.add(score)

    second_lowest = sortes(scores)[1]
    print(*sorted([name for name, score in Students if score==second_lowest]),sep='\n')

