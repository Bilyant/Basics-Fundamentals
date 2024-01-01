import math

initial_group_size = int(input())
days = int(input())
current_group_size = initial_group_size

coins = 0

for day in range(1, days + 1):
    motivational_party = False
    if day % 10 == 0:
        current_group_size -= 2
    if day % 15 == 0:
        current_group_size += 5
    coins += 50
    coins -= current_group_size * 2  # for food

    if day % 3 == 0:
        motivational_party = True
        coins -= current_group_size * 3

    if day % 5 == 0:
        coins += 20 * current_group_size
        if motivational_party:
            coins -= current_group_size * 2

coins_per_companion = math.floor(coins / current_group_size)
print(f'{current_group_size} companions received {coins_per_companion} coins each.')
