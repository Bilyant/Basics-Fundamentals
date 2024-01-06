data = input()
data = data.replace(' ', '')
data = [el for el in data]
dict = {}

for char in data:
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] += 1

for char, count in dict.items():
    print(f'{char} -> {count}')
