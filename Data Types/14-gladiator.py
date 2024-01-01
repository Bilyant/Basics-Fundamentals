lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_broken = 0

for lost_fight in range(1, lost_fights + 1):
    sword_is_broken = False
    helmet_is_broken = False
    if lost_fight % 2 == 0:
        helmet_is_broken = True
        expenses += helmet_price
    if lost_fight % 3 == 0:
        sword_is_broken = True
        expenses += sword_price

    if sword_is_broken and helmet_is_broken:
        expenses += shield_price
        shield_broken += 1
        if shield_broken == 2:
            expenses += armor_price
            shield_broken = 0

print(f'Gladiator expenses: {expenses:.2f} aureus')
