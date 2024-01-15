import sys
from collections import deque

cols, rows = [int(n) for n in input().split()]
max_sum = -sys.maxsize
matrix = []
max_matrix_elements = []

for _ in range(cols):
    matrix.append([int(n) for n in input().split()])

for col_idx in range(cols-2):
    for row_idx in range(rows - 2):
        current_matrix = [matrix[col_idx][row_idx], matrix[col_idx][row_idx + 1], matrix[col_idx][row_idx + 2],
                          matrix[col_idx+1][row_idx], matrix[col_idx+1][row_idx+1], matrix[col_idx+1][row_idx+2],
                          matrix[col_idx+2][row_idx], matrix[col_idx+2][row_idx+1], matrix[col_idx+2][row_idx+2]]
        if sum(current_matrix) > max_sum:
            max_sum = sum(current_matrix)
            max_matrix_elements = current_matrix

print(f'Sum = {max_sum}')
max_matrix_elements = deque(max_matrix_elements)
while max_matrix_elements:
    for i in range(3):
        print(f'{max_matrix_elements.popleft()} {max_matrix_elements.popleft()} {max_matrix_elements.popleft()}')
