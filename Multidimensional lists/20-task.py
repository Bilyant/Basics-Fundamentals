size = int(input())
matrix = []
removed_pieces = 0
have_attacks = True

for _ in range(size):
    matrix.append([ch for ch in input()])

knight_moves = {
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
}

while have_attacks:
    knight_attacks = {}
    for row_idx in range(size):
        for col_idx in range(size):
            attacks = 0
            if matrix[row_idx][col_idx] == 'K':
                knight_attacks[(row_idx, col_idx)] = 0
                for r, c in knight_moves:
                    current_row = row_idx + r
                    current_col = col_idx + c
                    if (0 <= current_row < size) and (0 <= current_col < size):
                        if matrix[current_row][current_col] == 'K':
                            attacks += 1
            knight_attacks[(row_idx, col_idx)] = attacks

    attacks_all = [n for n in knight_attacks.values() if n > 0]
    knight_to_remove = ()
    if attacks_all:
        max_attack = max(attacks_all)
        for coord, value in knight_attacks.items():
            if value == max_attack:
                c, r = coord
                knight_to_remove = (c, r)

        knight_attacks.pop(knight_to_remove)
        r, c = knight_to_remove[0], knight_to_remove[1]
        matrix[r][c] = '0'
        removed_pieces += 1
    else:
        break

print(removed_pieces)
