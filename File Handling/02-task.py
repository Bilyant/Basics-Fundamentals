try:
    with open('numbers.txt', 'r') as file:
        print(sum([int(n) for n in file.readlines()]))
except FileNotFoundError:
    print('File not found')

# file = open('numbers.txt')
# [print(line, end='') for line in file.readlines()]

with open('numbers.txt') as file:
    for line in file:
        print(int(line))
