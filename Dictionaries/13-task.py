number = int(input())
register = {}

for i in range(number):
    data = input().split()
    command = data[0]

    if command == 'register':
        name, number = data[1], data[2]
        if name in register:
            print(f'ERROR: already registered with plate number {number}')
            continue

        register[name] = number
        print(f'{name} registered {number} successfully')

    elif command == 'unregister':
        name = data[1]

        if name not in register:
            print(f'ERROR: user {name} not found')
            continue

        register.pop(name)
        print(f'{name} unregistered successfully')

for name, number in register.items():
    print(f'{name} => {number}')
