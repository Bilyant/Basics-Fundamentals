number = int(input())
characters = []
total = 0

for i in range(number):
    char = input()
    characters.append(char)
    total += ord(char)

print(f'The sum equals: {total}')
