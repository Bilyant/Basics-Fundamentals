from collections import deque

materials_values = [int(n) for n in input().split()]
magic_values = deque(int(n) for n in input().split())
toys_crafted = []
toy_prices = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

while materials_values and magic_values:
    materials_box = materials_values[-1]
    magic_value = magic_values[0]
    magic_crafted = materials_box * magic_value

    if magic_crafted in toy_prices:
        toys_crafted.append(toy_prices[magic_crafted])
        materials_values.pop()
        magic_values.popleft()

    elif magic_crafted < 0:
        sum_value = materials_box + magic_value
        materials_values.pop()
        magic_values.popleft()
        materials_values.append(sum_value)

    elif materials_box == 0 or magic_value == 0:
        if materials_box == 0:
            materials_values.pop()
        elif magic_value == 0:
            magic_values.popleft()

    elif materials_box > 0 and magic_value > 0:
        magic_values.popleft()
        materials_values[-1] += 15

presents_are_crafted = False
if ('Doll' in toys_crafted and 'Wooden train' in toys_crafted or
        'Teddy bear' in toys_crafted and 'Bicycle' in toys_crafted):
    presents_are_crafted = True

if presents_are_crafted:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials_values:
    result = []
    while materials_values:
        result.append(str(materials_values.pop()))
    print(f'Materials left: {", ".join(result)}')
if magic_values:
    result = []
    while magic_values:
        result.append(str(magic_values.popleft()))
    print(f'Magic left: {", ".join(result)}')

if toys_crafted:
    toys_crafted = sorted(toys_crafted)
    toys_total = {}
    for toy in toys_crafted:
        if toy not in toys_total:
            toys_total[toy] = 0
        toys_total[toy] += 1
    for toy, count in toys_total.items():
        print(f'{toy}: {count}')
