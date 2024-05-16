grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average_grades = [sum(i) / len(i) for i in grades]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()

average_results = dict(zip(students_list, average_grades))
print(average_results)
