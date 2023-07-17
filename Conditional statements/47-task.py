month = input()
nights_count = int(input())
studio_price_per_night = 0
flat_price_per_night = 0
if month == "May" or month == "October":
    studio_price_per_night = 50
    flat_price_per_night = 65
    if 7 < nights_count < 14:
        studio_price_per_night *= 0.95
    elif nights_count > 14:
        studio_price_per_night *= 0.7
elif month == "June" or month == "September":
    studio_price_per_night = 75.2
    flat_price_per_night = 68.7
    if nights_count > 14:
        studio_price_per_night *= 0.8
elif month == "July" or month == "August":
    studio_price_per_night = 76
    flat_price_per_night = 77
if nights_count > 14:
    flat_price_per_night *= 0.9
print(f"Apartment: {nights_count * flat_price_per_night:.2f} lv.")
print(f"Studio: {nights_count * studio_price_per_night:.2f} lv.")
