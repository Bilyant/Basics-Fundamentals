days_count_residence = int(input()) - 1
type_of_residency = input()
atanas_review = input()
room_for_one_person_per_night = 18
apartment_per_night = 25
president_apartment_per_night = 35
budget_required = 0
if type_of_residency == "room for one person":
    budget_required = room_for_one_person_per_night * days_count_residence
elif type_of_residency == "apartment":
    if days_count_residence < 10:
        apartment_per_night *= 0.7
        budget_required = apartment_per_night * days_count_residence
    elif 10 <= days_count_residence <= 15:
        apartment_per_night *= 0.65
        budget_required = apartment_per_night * days_count_residence
    else:
        apartment_per_night *= 0.5
        budget_required = apartment_per_night * days_count_residence
elif type_of_residency == "president apartment":
    if days_count_residence < 10:
        president_apartment_per_night *= 0.9
        budget_required = president_apartment_per_night * days_count_residence
    elif 10 <= days_count_residence <= 15:
        president_apartment_per_night *= 0.85
        budget_required = president_apartment_per_night * days_count_residence
    else:
        president_apartment_per_night *= 0.8
        budget_required = president_apartment_per_night * days_count_residence
if atanas_review == "positive":
    budget_required *= 1.25
elif atanas_review == "negative":
    budget_required *= 0.9
print(f"{budget_required:.2f}")
