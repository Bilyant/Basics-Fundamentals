numbers = [int(n) for n in input().split(' ')]
filtered = []

for number in numbers:
    if number >= 0:
        filtered.append(-number)
    else:
        filtered.append(abs(number))

print(filtered)
