number_of_orders = int(input())
total_price = 0

for day in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    price = (capsules_count * price_per_capsule) * days
    total_price += price
    if price > 0:
        print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total_price:.2f}')
