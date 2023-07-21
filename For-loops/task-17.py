groups_count = int(input())
group_musala = 0
group_monblan = 0
group_kilimanjaro = 0
group_k2 = 0
group_everest = 0
total_people = 0
for number in range(groups_count):
    current_group = int(input())
    total_people += current_group
    if current_group <= 5:
        group_musala += current_group
    elif current_group < 13:
        group_monblan += current_group
    elif current_group < 26:
        group_kilimanjaro += current_group
    elif current_group < 41:
        group_k2 += current_group
    else:
        group_everest += current_group
group_musala_percent = (group_musala / total_people) * 100
group_monblan_percent = group_monblan / total_people * 100
group_kilimanjaro_percent = group_kilimanjaro / total_people * 100
group_k2_percent = group_k2 / total_people * 100
group_everest_percent = group_everest / total_people * 100
print(f"{group_musala_percent:.2f}%")
print(f"{group_monblan_percent:.2f}%")
print(f"{group_kilimanjaro_percent:.2f}%")
print(f"{group_k2_percent:.2f}%")
print(f"{group_everest_percent:.2f}%")
