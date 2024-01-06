items = {
    "shards":"Shadowmourne",
    "fragments":"Valanyr",
    "motes":"Dragonwrath",
}
key_materials = {
    'shards': 0,
    'fragments': 0,
    'motes': 0,
}
junk_materials = {}
item_is_won = False
key_resource = ''

line = input()

while line:
    data = line.split()
    for i in range(0, len(data), 2):
        quantity = int(data[i])
        resource = data[i + 1].lower()

        if resource in key_materials:
            key_materials[resource] += quantity

            if key_materials[resource] >= 250:
                key_materials[resource] -= 250
                item_is_won = True
                key_resource = resource
                break
        else:
            if resource not in junk_materials:
                junk_materials[resource] = 0
            junk_materials[resource] += quantity

    if item_is_won:
        break
    line = input()

if item_is_won:
    won_item = items[key_resource]
    print(f'{won_item} obtained!')
    for resource, quantity in key_materials.items():
        print(f'{resource}: {quantity}')
    for resource, quantity in junk_materials.items():
        print(f'{resource}: {quantity}')