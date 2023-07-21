student_name = input()
current_class = 0
average_grade = 0
fails_counter = 0
grades_sum = 0
is_failed = False
while current_class < 12:
    current_grade = float(input())
    if current_grade < 4:
        fails_counter += 1
        if fails_counter == 2:
            is_failed = True
            break
    grades_sum += current_grade
    current_class += 1
if is_failed:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = grades_sum / current_class
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
