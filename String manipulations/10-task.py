text = input().split()
filtered = [el for el in text if el[0] == ':']
result = [el[:2] for el in filtered]
print('\n'.join(result))
