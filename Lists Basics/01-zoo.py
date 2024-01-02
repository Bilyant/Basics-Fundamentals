items = []

for i in range(3):
    item = input()
    items.append(item)

items[0], items[2] = items[2], items[0]

print(items)
