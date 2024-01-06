data = list(map(lambda x: x.lower(), input().split()))
occurrences = {i: data.count(i) for i in data}
result = []
for key, value in occurrences.items():
    if value % 2 != 0:
        result.append(key)

print(' '.join(result))
