line = input()
# special_commands = ['special', 'regular']
price_no_taxes = 0
total_price = 0
valid_order = True

# while line not in special_commands:
while line != 'special' or line != 'regular':
    price = float(line)
    if price < 0:
        print('Invalid price!')
        line = input()
        continue
    price_no_taxes += price
    line = input()

taxes = price_no_taxes * 0.2
total_price = price_no_taxes + taxes

if total_price == 0:
    print('Invalid order!')
    valid_order = False

if valid_order:
    if line == 'special':
        total_price -= total_price * 0.10
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {price_no_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')
