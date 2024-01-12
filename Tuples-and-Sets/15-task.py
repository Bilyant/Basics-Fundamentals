from collections import deque

worker_bees = deque(int(x) for x in input().split())
nectar_values = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())
total_honey_made = 0

while nectar_values and worker_bees:
    bee_load = worker_bees[0]
    nectar_value = nectar_values[-1]
    if nectar_value >= bee_load:
        calc_symbol = symbols.popleft()
        current_honey_made = 0
        if calc_symbol == '+':
            current_honey_made = bee_load + nectar_value
        elif calc_symbol == '-':
            current_honey_made = bee_load - nectar_value
        elif calc_symbol == '*':
            current_honey_made = bee_load * nectar_value
        elif calc_symbol == '/':
            current_honey_made = bee_load / nectar_value
        total_honey_made += abs(current_honey_made)
        worker_bees.popleft()
        nectar_values.pop()
    else:
        nectar_values.pop()

print(f'Total honey made: {total_honey_made}')
if worker_bees:
    print(f'Bees left: {", ".join([str(bee) for bee in worker_bees])}')
if nectar_values:
    print(f'Nectar left: {", ".join([str(n) for n in nectar_values])}')
