quantity_for_decoration = int(input())
days_until_christmas = int(input())
cost = 0
spirit = 0

# prices per piece
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity_for_decoration += 2

    if day % 2 == 0:
        spirit += 5
        cost += ornament_set * quantity_for_decoration

    if day % 3 == 0:
        spirit += 13
        cost += (quantity_for_decoration * tree_skirt) + (quantity_for_decoration * tree_garland)

    if day % 5 == 0:
        spirit += 17
        cost += quantity_for_decoration * tree_lights
        if day % 3 == 0:
            spirit += 30

    if day % 10 == 0:
        spirit -= 20
        cost += tree_skirt + tree_garland + tree_lights

if days_until_christmas % 10 == 0:
    spirit -= 30

print(f'Total cost: {cost}')
print(f'Total spirit: {spirit}')
