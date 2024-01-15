cols, rows = [int(n) for n in input().split()]
square_matrices = 0
matrix = []

for _ in range(cols):
    matrix.append(input().split())

for col_idx in range(cols-1):
    for row_idx in range(rows - 1):
        current_square = [matrix[col_idx][row_idx], matrix[col_idx][row_idx+1], matrix[col_idx+1][row_idx], matrix[col_idx+1][row_idx+1]]
        if len(set(current_square)) == 1:
            square_matrices += 1

print(square_matrices)
