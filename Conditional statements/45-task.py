budget_available = float(input())
season = input()
budget_required = 0
destination = ""
accommodation_type = ""
if budget_available <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget_required = budget_available * 0.3
        accommodation_type = "Camp"
    elif season == "winter":
        budget_required = budget_available * 0.7
        accommodation_type = "Hotel"
elif 100 < budget_available <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget_required = budget_available * 0.4
        accommodation_type = "Camp"
    elif season == "winter":
        budget_required = budget_available * 0.8
        accommodation_type = "Hotel"
else:
    destination = "Europe"
    budget_required = budget_available * 0.9
    accommodation_type = "Hotel"
print(f"Somewhere in {destination}")
print(f"{accommodation_type} - {budget_required:.2f}")
