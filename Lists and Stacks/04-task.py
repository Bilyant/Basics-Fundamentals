from collections import deque

quantity = int(input())
line = input()
names = deque()

while line != 'Start':
    names.append(line)
    line = input()

line = input()
while line != 'End':
    if line.isnumeric():
        name = names.popleft()
        water = int(line)
        if quantity >= water:
            quantity -= water
            print(f'{name} got water')
        else:
            print(f'{name} must wait')
    elif 'refill' in line:
        command, liters = line.split()
        quantity += int(liters)

    line = input()

print(f'{quantity} liters left')
