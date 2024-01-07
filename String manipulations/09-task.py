data = [ch for ch in input()]
result = ''

for char in data:
    num = ord(char)
    result += chr(num + 3)

print(result)
