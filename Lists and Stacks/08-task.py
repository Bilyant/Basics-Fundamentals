from collections import deque

food_quantity = int(input())
orders = deque(int(n) for n in input().split())
biggest_order = max(orders)

while orders:
    order = orders[0]
    if food_quantity >= order:
        food_quantity -= orders.popleft()
    else:
        break

print(biggest_order)
if orders:
    print(f'Orders left: {" ".join([str(x) for x in orders])}')
else:
    print('Orders complete')
