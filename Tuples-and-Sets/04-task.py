number = int(input())
car_numbers = set()

for _ in range(number):
    line = input().split(', ')
    command, car_number = line[0], line[1]
    if command == 'IN':
        car_numbers.add(car_number)
    elif command == 'OUT':
        if car_number in car_numbers:
            car_numbers.remove(car_number)

if car_numbers:
    print(*car_numbers, sep='\n')
else:
    print('Parking Lot is Empty')
