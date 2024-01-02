fires = input().split('#')
water = int(input())
total_effort = 0
total_fire = 0
cells_result = []

for fire in fires:
    fire_type, value = fire.split(' = ')
    value = int(value)

    if fire_type == 'High':
        if 81 <= value <= 125:
            if water >= value:
                water -= value
                total_fire += value
                total_effort += 0.25 * value
                cells_result.append(value)
    if fire_type == 'Medium':
        if 51 <= value <= 80:
            if water >= value:
                water -= value
                total_fire += value
                total_effort += 0.25 * value
                cells_result.append(value)

    if fire_type == 'Low':
        if 1 <= value <= 50:
            if water >= value:
                water -= value
                total_fire += value
                total_effort += 0.25 * value
                cells_result.append(value)

print('Cells:')
for cell in cells_result:
    print(f'- {cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
