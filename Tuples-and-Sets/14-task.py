from collections import deque

chocolates_as_stack = [int(x) for x in input().split(', ')]
milk_cups = deque(int(x) for x in input().split(', '))
milkshakes = 0

while chocolates_as_stack and milk_cups and milkshakes < 5:
    choco_value = chocolates_as_stack[-1]
    milk_value = milk_cups[0]

    if choco_value <= 0:
        chocolates_as_stack.pop()
        continue
    if milk_value <= 0:
        milk_cups.popleft()
        continue

    if choco_value == milk_value:
        milkshakes += 1
        choco_value = chocolates_as_stack.pop()
        milk_value = milk_cups.popleft()
    else:
        milk_cups.append(milk_cups.popleft())
        chocolates_as_stack[-1] -= 5
        if chocolates_as_stack[-1] <= 0:
            chocolates_as_stack.pop()


if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolates_as_stack:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates_as_stack)}")
else:
    print('Chocolate: empty')
if milk_cups:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print('Milk: empty')

