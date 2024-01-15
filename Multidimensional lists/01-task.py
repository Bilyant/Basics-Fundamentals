rows, cols = [int(n) for n in input().split(', ')]
matrix = []
total = 0

for _ in range(rows):
    line = [int(num) for num in input().split(', ')]
    total += sum(line)
    matrix.append(line)

print(total)
print(matrix)
