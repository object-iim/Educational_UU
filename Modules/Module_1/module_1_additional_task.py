grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_of_students = list(students)
sort_list_of_students = sorted(list(students))

gp_aaron = sum(grades[0]) / len(grades[0])
gp_bilbo = sum(grades[1]) / len(grades[1])
gp_johnny = sum(grades[2]) / len(grades[2])
gp_khendrik = sum(grades[3]) / len(grades[3])
gp_steve = sum(grades[4]) / len(grades[4])
grade_point = {sort_list_of_students[0]: float(gp_aaron),
               sort_list_of_students[1]: float(gp_bilbo),
               sort_list_of_students[2]: float(gp_johnny),
               sort_list_of_students[3]: float(gp_khendrik),
               sort_list_of_students[4]: float(gp_steve)}
print(grade_point)

# Исправленный вариант
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(students)

gp_aaron = sum(grades[0]) / len(grades[0])
gp_bilbo = sum(grades[1]) / len(grades[1])
gp_johnny = sum(grades[2]) / len(grades[2])
gp_khendrik = sum(grades[3]) / len(grades[3])
gp_steve = sum(grades[4]) / len(grades[4])
grade_point = {students[0]: (gp_aaron),
               students[1]: (gp_bilbo),
               students[2]: (gp_johnny),
               students[3]: (gp_khendrik),
               students[4]: (gp_steve)}
print(grade_point)