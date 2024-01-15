size = int(input())
matrix = []
primary_diagonal_nums = []
secondary_diagonal_nums = []

for _ in range(size):
    matrix.append([int(n) for n in input().split(', ')])

for i in range(1, size + 1):
    primary_diagonal_nums.append(matrix[i-1][i-1])
    secondary_diagonal_nums.append(matrix[i-1][size-i])

print(f'Primary diagonal: {", ".join([str(n) for n in primary_diagonal_nums])}. Sum: {sum(primary_diagonal_nums)}')
print(f'Secondary diagonal: {", ".join([str(n) for n in secondary_diagonal_nums])}. Sum: {sum(secondary_diagonal_nums)}')
