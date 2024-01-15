import sys
from collections import deque

rows, cols = [int(n) for n in input().split(', ')]
biggest_sum = -sys.maxsize
biggest_square_coordinates = []
matrix = []

for _ in range(rows):
    line = [int(ch) for ch in input().split(', ')]
    matrix.append(line)


for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        if matrix[row_idx][col_idx]:
            current_square_matrix = [matrix[row_idx][col_idx], matrix[row_idx][col_idx + 1], matrix[row_idx + 1][col_idx], matrix[row_idx + 1][col_idx + 1]]
            current_sum = sum(current_square_matrix)
            if current_sum > biggest_sum:
                biggest_sum = current_sum
                biggest_square_coordinates = current_square_matrix.copy()

print(biggest_square_coordinates[0], biggest_square_coordinates[1])
print(biggest_square_coordinates[2], biggest_square_coordinates[3])
print(biggest_sum)
