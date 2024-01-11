from collections import deque

line = input()
customers = deque()

while line != 'End':
    if line == 'Paid':
        if customers:
            while customers:
                print(customers.popleft())
        line = input()
        continue
    customers.append(line)
    line = input()

print(f'{len(customers)} people remaining.')
