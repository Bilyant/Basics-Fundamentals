def absolute_values(list):
    return [abs(n) for n in numbers]


numbers = [float(n) for n in input().split(' ')]
result = absolute_values(numbers)
print(result)
