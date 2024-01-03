def get_grade(grade: float):
    result = ''
    if grade >= 2 and grade <= 2.99:
        result = 'Fail'
    elif grade >= 3 and grade <= 3.49:
        result = 'Poor'
    elif grade >= 3.50 and grade <= 4.49:
        result = 'Good'
    elif grade >= 4.50 and grade <= 5.49:
        result = 'Very Good'
    elif grade >= 5.50 and grade <= 6.00:
        result = 'Excellent'
    return result


grade = float(input())
print(get_grade(grade))
