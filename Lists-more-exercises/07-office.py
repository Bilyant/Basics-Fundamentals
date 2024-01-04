employees_happiness = list(map(int, input().split()))
factor = int(input())
multiplied_by_factor = list(map(lambda em: em * factor, employees_happiness))
average_happiness = sum(multiplied_by_factor) / len(employees_happiness)
greater_than_average = list(filter(lambda  em: em >= average_happiness, multiplied_by_factor))
are_happier = len(greater_than_average) >= len(employees_happiness) // 2

if are_happier:
    print(f'Score: {len(greater_than_average)}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(greater_than_average)}/{len(employees_happiness)}. Employees are not happy!')
