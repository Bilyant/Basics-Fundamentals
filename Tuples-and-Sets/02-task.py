number = int(input())
students = {}

for _ in range(number):
    line = input().split()
    name, grade = line[0], float(line[1])
    if name not in students:
        students[name] = []
    students[name].append(f'{grade:.2f}')

for name, grades in students.items():
    str_grades = ' '.join(str(x) for x in grades)
    average_grade = sum([float(x) for x in grades]) / len(grades)
    print(f'{name} -> {str_grades} (avg: {average_grade:.2f})')
