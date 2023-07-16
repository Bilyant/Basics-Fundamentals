city = input()
sells_volume = float(input())
sells = 0
is_Valid = False
if city == "Sofia":
    is_Valid = True
    if sells_volume <= 500:
        sells = sells_volume * 0.05
    elif 500 < sells_volume <= 1000:
        sells = sells_volume * 0.07
    elif 1000 < sells_volume <= 10000:
        sells = sells_volume * 0.08
    elif sells_volume > 10000:
        sells = sells_volume * 0.12
elif city == "Varna":
    is_Valid = True
    if sells_volume <= 500:
        sells = sells_volume * 0.045
    elif 500 < sells_volume <= 1000:
        sells = sells_volume * 0.075
    elif 1000 < sells_volume <= 10000:
        sells = sells_volume * 0.1
    elif sells_volume > 10000:
        sells = sells_volume * 0.13
elif city == "Plovdiv":
    is_Valid = True
    if sells_volume <= 500:
        sells = sells_volume * 0.055
    elif 500 < sells_volume <= 1000:
        sells = sells_volume * 0.08
    elif 1000 < sells_volume <= 10000:
        sells = sells_volume * 0.12
    elif sells_volume > 10000:
        sells = sells_volume * 0.145
if is_Valid and sells_volume > 0:
    print(f"{sells:.2f}")
else:
    print("error")
