from collections import deque

numbers = deque(int(n) for n in input().split())
capacity = int(input())
racks = 1
total = 0

while numbers:
    number = numbers[0]
    if total + number <= capacity:
        total += numbers.popleft()
    else:
        racks += 1
        total = 0

print(racks)
