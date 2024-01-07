data = input().split()
total = 0
shorter_item = ''.join(data[0] if len(data[0]) < len(data[1]) else [data[1]])
longer_item = ''.join(data[1] if len(data[1]) > len(data[0]) else [data[0]])
loops = len(shorter_item) if len(shorter_item) == len(longer_item) else len(shorter_item) + 1

for i in range(loops):
    if i == len(shorter_item) and len(shorter_item) < len(longer_item):
        for char in longer_item[i:]:
            total += ord(char)
    else:
        total += ord(shorter_item[i]) * ord(longer_item[i])

print(total)
