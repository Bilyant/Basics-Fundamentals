phonebook = {}
line = input()

while not line.isdigit():
    data = line.split('-')
    name, number = data[0], data[1]
    phonebook[name] = number
    line = input()

number = int(line)

for i in range(number):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
