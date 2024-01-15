rows, cols = [int(num) for num in input().split()]
matrix = []
middle_char = 97

for row_idx in range(rows):
    row = []
    for col_idx in range(cols):
        item = chr(97 + row_idx) + chr(middle_char + col_idx) + chr(97 + row_idx)
        row.append(item)
    matrix.append(row)
    middle_char += 1

for row in matrix:
    print(*row)
