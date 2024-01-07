strings = input().split()
result = list(map(lambda s: s * len(s), strings))
print(''.join(result))
