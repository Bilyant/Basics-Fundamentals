factor = int(input())
count = int(input())
numbers = []

while len(numbers) < count:
    for i in range(factor, factor * count + 1):
        if i % factor == 0:
            numbers.append(i)

print(numbers)
