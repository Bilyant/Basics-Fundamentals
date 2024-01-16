data = [el.strip() for el in input().split('|')]
result = []

for i in range(len(data) - 1, -1, -1):
    for item in data[i].split():
        elements = item.split()
        result.extend([ch for ch in elements if ch != ''])

print(*result)
