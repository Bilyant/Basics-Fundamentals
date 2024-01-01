numbers = list()

for num in range(4):
    numbers.append(int(input()))

result = ((numbers[0] + numbers[1]) // numbers[2]) * numbers[3]
print(result)
