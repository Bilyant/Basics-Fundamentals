budget_available = int(input())
season = input()
fishermen_count = int(input())
boat_rent = 0
if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600
if fishermen_count <= 6:
    boat_rent *= 0.9
elif 7 <= fishermen_count <= 11:
    boat_rent *= 0.85
elif fishermen_count >= 12:
    boat_rent *= 0.75
if not season == "Autumn" and fishermen_count % 2 == 0:
    boat_rent *= 0.95
difference = abs(budget_available - boat_rent)
if budget_available >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
    