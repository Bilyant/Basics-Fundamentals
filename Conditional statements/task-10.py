hour = int(input())
current_minutes = int(input())
minutes_plus_15 = current_minutes + 15
if minutes_plus_15 > 59:
    minutes_plus_15 = minutes_plus_15 % 60
    hour += 1
if hour > 23:
    hour = 0
if minutes_plus_15 < 10:
    print(f"{hour}:0{minutes_plus_15}")
else:
    print(f"{hour}:{minutes_plus_15}")
