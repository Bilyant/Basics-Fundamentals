size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(n) for n in input().split()])

line = input()

while line != 'END':
    data = line.split()
    row, col, value = [int(n) for n in data[1:]]
    # if (row >= 0 and row < size) and (col >= 0 and col < size):
    if (0 <= row < size) and (0 <= col < size):
        if data[0] == 'Add':
            matrix[row][col] += value
        elif data[0] == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
    line = input()

for row in matrix:
    print(*row)
