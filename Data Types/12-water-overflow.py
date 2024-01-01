number = int(input())
capacity = 255
current_quantity = 0

for i in range(number):
    water = int(input())
    if current_quantity + water > capacity:
        print('Insufficient capacity!')
    else:
        current_quantity += water

print(current_quantity)
