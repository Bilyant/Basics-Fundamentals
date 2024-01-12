data = tuple(float(el) for el in input().split())
elements = []

for el in data:
    if el not in elements:
        print(f'{el:.1f} - {data.count(el)} times')
    elements.append(el)

