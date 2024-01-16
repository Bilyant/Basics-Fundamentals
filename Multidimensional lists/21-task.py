size = int(input())
matrix = []
bunny_coord = []
directions = {
    (-1, 0): 'up',
    (1, 0): 'down',
    (0, 1): 'right',
    (0, -1): 'left',
}
total_eggs_collected = {}
best_direction_coord = {}

for row_idx in range(size):
    line = [ch for ch in input().split()]
    for col_idx in range(len(line)):
        if line[col_idx] == 'B':
            bunny_coord = [row_idx, col_idx]
    matrix.append(line)

for coord, direction in directions.items():
    current_r = bunny_coord[0] + coord[0]
    current_c = bunny_coord[1] + coord[1]
    current_direction = direction
    total_eggs_collected[current_direction] = 0
    best_direction_coord[current_direction] = []
    change_direction = False
    while not change_direction:
        if (0 <= current_r < size) and (0 <= current_c < size):  # valid coord
            if matrix[current_r][current_c] != 'X':
                total_eggs_collected[current_direction] += int(matrix[current_r][current_c])
                best_direction_coord[current_direction].append((current_r, current_c))
            else:
                change_direction = True
        else:
            change_direction = True
        current_r += coord[0]
        current_c += coord[1]

# output
max_eggs_collected = max([x for x in total_eggs_collected.values()])
best_direction = ''
for direct, eggs_count in total_eggs_collected.items():
    if max_eggs_collected == eggs_count:
        best_direction = direct
        break
print(best_direction)
for coord in best_direction_coord[best_direction]:
    print(list(coord))
print(max_eggs_collected)
