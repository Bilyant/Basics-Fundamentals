def round_numbers(numbers: list):
    return [round(x) for x in numbers]


numbers = [float(x) for x in input().split(' ')]
print(round_numbers((numbers)))
