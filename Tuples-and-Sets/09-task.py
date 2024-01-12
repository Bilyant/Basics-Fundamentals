data = tuple(ch for ch in input())
result = set()

for ch in data:
    result.add(f'{ch}: {data.count(ch)} time/s')

print(*sorted(result), sep='\n')
