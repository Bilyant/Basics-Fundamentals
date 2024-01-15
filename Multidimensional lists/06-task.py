number = int(input())
is_found = False
coordinates = None
matrix = []

for _ in range(number):
    line = [ch for ch in input()]
    matrix.append(line)

searched_char = input()

for row_idx in range(number):
    for col_idx in range(number):
        if matrix[row_idx][col_idx] == searched_char:
            is_found = True
            coordinates = f'({row_idx}, {col_idx})'
            break
    if is_found:
        break

if is_found:
    print(coordinates)
else:
    print(f'{searched_char} does not occur in the matrix')
