size = int(input())
matrix = []
alice_coord = []
rabbit_hole_coord = []
tea_bags_collected = 0
failed = False
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row_idx in range(size):
    line = [ch for ch in input().split()]
    matrix.append(line)
    for col_idx in range(len(line)):
        if matrix[row_idx][col_idx] == 'A':
            matrix[row_idx][col_idx] = '*'
            alice_coord = [row_idx, col_idx]
        elif matrix[row_idx][col_idx] == 'R':
            rabbit_hole_coord = [row_idx, col_idx]

command = input()

while command:
    r, c = directions[command]
    current_r = alice_coord[0] + r
    current_c = alice_coord[1] + c
    if (0 <= current_r < size) and (0 <= current_c < size):  # valid coord
        if matrix[current_r][current_c].isdigit():
            tea_bags_collected += int(matrix[current_r][current_c])
        elif matrix[current_r][current_c] == 'R':
            matrix[current_r][current_c] = '*'
            failed = True
            break
        matrix[current_r][current_c] = '*'
        alice_coord = [current_r, current_c]
    else:
        failed = True
        break
    command = input()

if failed:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row, sep=' ')
