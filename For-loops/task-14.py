age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())
birthday_money = 0
toys_count = 0
toys_money = 0
brother_money = 0
for number in range(1, age + 1):
    if number % 2 == 0:
        birthday_money += number / 2 * 10
        brother_money += 1
    else:
        toys_count += 1
        toys_money = toys_count * price_per_toy
saved_money = birthday_money + toys_money - brother_money
difference = abs(saved_money - washing_machine_price)
if saved_money >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
