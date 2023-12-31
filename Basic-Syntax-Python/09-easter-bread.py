budget = float(input())
flour_price_per_kg = float(input())

colored_eggs = 0
easter_bread_count = 0

eggs_price_per_pack = 0.75 * flour_price_per_kg
milk_price_per_lt = 1.25 * flour_price_per_kg
milk_price_per_recipe = milk_price_per_lt / 4
price_per_easter_bread = eggs_price_per_pack + milk_price_per_recipe + flour_price_per_kg

while budget >= price_per_easter_bread:
    budget -= price_per_easter_bread
    easter_bread_count += 1
    colored_eggs += 3
    if easter_bread_count % 3 == 0:
        colored_eggs -= easter_bread_count - 2

print(f'You made {easter_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
