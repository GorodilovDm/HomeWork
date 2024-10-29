grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
aver_score = {}
for i in range(len(students)):
    aver_score[students[i]] = sum(grades[i])/len(grades[i])
print(aver_score)