def do_damage(damage, row, col):
    for item in rows_cols:
        r, c = item
        current_row = row + r
        current_col = col + c
        if (current_row >= 0 and current_row < size) and (current_col >= 0 and current_col < size):
            if matrix[current_row][current_col] != 'X' and matrix[current_row][current_col] > 0:
                matrix[current_row][current_col] -= damage


size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(n) for n in input().split()])

coordinates = input().split()

rows_cols = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, +1),
    (1, -1),
    (1, 0),
    (1, 1),
]

for el in coordinates:
    row, col = [int(num) for num in el.split(',')]
    damage_points = matrix[row][col]
    matrix[row][col] = 'X'
    do_damage(damage_points, row, col)

alive_cells = []

for row_idx in range(size):
    for col_idx in range(size):
        if matrix[row_idx][col_idx] == 'X':
            matrix[row_idx][col_idx] = 0
    alive_cells.extend([x for x in matrix[row_idx] if x > 0])

print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')
for row in matrix:
    print(*row)
