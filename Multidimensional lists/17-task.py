def draw_bunnies(new_bunnies):
    for element in new_bunnies:
        for r, c in element:
            if matrix[r][c] != 'B':
                matrix[r][c] = 'B'


def multiply_bunnies(player_coord: []):
    new_bunnies = []
    player_alive = True
    for row_idx in range(rows):
        for col_idx in range(cols):
            if matrix[row_idx][col_idx] == 'B':
                current_new_bunnies = []

                for r, c in directions.values():
                    current_r = r + row_idx
                    current_c = c + col_idx
                    if (current_r >= 0 and current_r < rows) and (current_c >= 0 and current_c < cols):
                        if matrix[current_r][current_c] == 'P':
                            player_alive = False
                            matrix[current_r][current_c] = 'B'
                        elif matrix[current_r][current_c] == '.':
                            current_new_bunnies.append((current_r, current_c))
                    new_bunnies.append(current_new_bunnies)

            if not player_alive:
                break
        if not player_alive:
            break

    draw_bunnies(new_bunnies)
    return player_alive


from collections import deque

rows, cols = [int(num) for num in input().split()]
matrix = []
player_coord = []
game_over = True
player_wins = False
rabit_wins = False

directions = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
}

for row_idx in range(rows):
    line = [ch for ch in input()]
    for col_idx in range(len(line)):
        if line[col_idx] == 'P':
            player_coord.extend([row_idx, col_idx])
    matrix.append(line)

commands = deque([ch for ch in input()])

while commands:
    command = commands.popleft()
    r, c = directions[command]
    current_r, current_c = [player_coord[0] + r, player_coord[1] + c]

    if (current_r >= 0 and current_r < rows) and (current_c >= 0 and current_r < cols):  # valid coord
        if matrix[current_r][current_c] == 'B':
            player_coord = [current_r, current_c]
            multiply_bunnies(player_coord)
            rabit_wins = True
            break

    else:  # player wins - coord outside
        player_wins = True
        matrix[player_coord[0]][player_coord[1]] = '.'
        multiply_bunnies(player_coord)
        break

    matrix[player_coord[0]][player_coord[1]] = '.'
    player_coord = [current_r, current_c]
    matrix[current_r][current_c] = 'P'
    player_alive = multiply_bunnies([current_r, current_c])
    if not player_alive:
        matrix[player_coord[0]][player_coord[1]] = '.'
        rabit_wins = True
        break

for row in matrix:
    print(*row, sep='')
if player_wins:
    print(f'won: {" ".join(str(n) for n in player_coord)}')
else:
    print(f'dead: {" ".join(str(n) for n in player_coord)}')
