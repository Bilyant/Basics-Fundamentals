from collections import deque


def move(direction):
    valid_move = False
    r, c = directions_scheme[direction]
    current_row = minor_coord[0] + r
    current_col = minor_coord[1] + c
    if (current_row >= 0 and current_row < size) and (current_col >= 0 and current_col < size):
        minor_coord[0] = current_row
        minor_coord[1] = current_col
        valid_move = True
    return valid_move


size = int(input())
directions = deque(input().split())
matrix = []
coal_collected = 0
coal_count_total = 0
game_over = False
minor_coord = []

directions_scheme = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}

for _ in range(size):
    matrix.append([ch for ch in input().split()])

for row_idx in range(size):
    for col_idx in range(size):
        if matrix[row_idx][col_idx] == 's':
            minor_coord.extend([row_idx, col_idx])
        elif matrix[row_idx][col_idx] == 'c':
            coal_count_total += 1

while directions:
    direction = directions.popleft()
    next_step = move(direction)
    if next_step:
        if matrix[minor_coord[0]][minor_coord[1]] == 'c':
            coal_collected += 1
            if coal_collected == coal_count_total:
                break
            matrix[minor_coord[0]][minor_coord[1]] = '*'
        elif matrix[minor_coord[0]][minor_coord[1]] == 'e':
            game_over = True
            break

if game_over:
    print(f'Game over! {tuple(minor_coord)}')
elif coal_collected == coal_count_total:
    print(f'You collected all coal! {tuple(minor_coord)}')
else:
    print(f'{coal_count_total - coal_collected} pieces of coal left. {tuple(minor_coord)}')
