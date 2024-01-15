rows, cols = [int(num) for num in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

line = input()


def valid_line(line: []):
    is_valid = True
    command = line[0]
    if len(line) == 5 and command == 'swap':
        row1, col1, row2, col2 = [int(num) for num in line[1:]]
        if (row1 < 0 or row1 >= rows) or (row2 < 0 or row2 >= rows):
            is_valid = False
        if (col1 < 0 or col1 > cols) or (col2 < 0 or col2 > cols):
            is_valid = False
    else:
        is_valid = False

    return is_valid


while line != 'END':
    valid = valid_line(line.split())
    if valid:
        row1, col1, row2, col2 = [int(num) for num in line.split()[1:]]
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in matrix:
            print(*row)
    else:
        print('Invalid input!')
    line = input()



