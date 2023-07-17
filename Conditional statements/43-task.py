rose_single_price = 5
dahlia_single_price = 3.8
tulip_single_price = 2.8  # лале
narcissus_single_price = 3
gladiolus_single_price = 2.5
type_of_flowers = input()
flowers_count = int(input())
budget_available = int(input())
budget_required = 0
if type_of_flowers == "Roses":
    if flowers_count > 80:
        budget_required = 0.9 * (flowers_count * rose_single_price)
    else:
        budget_required = flowers_count * rose_single_price
elif type_of_flowers == "Dahlias":
    if flowers_count > 90:
        budget_required = 0.85 * (flowers_count * dahlia_single_price)
    else:
        budget_required = flowers_count * dahlia_single_price
elif type_of_flowers == "Tulips":
    if flowers_count > 80:
        budget_required = 0.85 * (flowers_count * tulip_single_price)
    else:
        budget_required = flowers_count * tulip_single_price
elif type_of_flowers == "Narcissus":
    if flowers_count < 120:
        budget_required = 1.15 * (flowers_count * narcissus_single_price)
    else:
        budget_required = flowers_count * narcissus_single_price
elif type_of_flowers == "Gladiolus":
    if flowers_count < 80:
        budget_required = 1.2 * (flowers_count * gladiolus_single_price)
    else:
        budget_required = flowers_count * gladiolus_single_price
difference = abs(budget_available - budget_required)
if budget_available >= budget_required:
    print(f"Hey, you have a great garden with {flowers_count} {type_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
