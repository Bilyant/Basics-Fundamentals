rows, cols = [int(n) for n in input().split(', ')]
matrix = []

for _ in range(rows):
    line = [int(n) for n in input().split()]
    matrix.append(line)

for rows_idx in range(cols):
    result = 0
    for cols_idx in range(rows):
        result += matrix[cols_idx][rows_idx]
    print(result)
