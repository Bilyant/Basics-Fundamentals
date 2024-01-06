stop_command = 'stop'
line = input()
dict = {}

while line != stop_command:

    resource = line
    if resource not in dict:
        dict[resource] = 0
    quantity = int(input())
    dict[resource] += quantity

    line = input()

for resource, quantity in dict.items():
    print(f'{resource} -> {quantity}')
