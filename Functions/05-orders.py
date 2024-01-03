prices = {
    'coffee': 1.5,
    'water': 1.00,
    'coke': 1.40,
    'snacks': 2.00,
}

order = input()
count = int(input())
calc_price = lambda order, count: prices[order] * count
print(f'{calc_price(order, count):.2f}')
