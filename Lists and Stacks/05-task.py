from collections import deque

data = input().split()
number = int(input())
names = deque(n for n in data)
last_name = None

while names:
    for n in range(number):
        names.append(names.popleft())
    last_name = names.pop()
    if names:
        print(last_name)

print(f'Last is {last_name}')
