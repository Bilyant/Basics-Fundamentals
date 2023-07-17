length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percents_occupied = float(input()) / 100

volume_cubic_m = length_cm * width_cm * height_cm
volume_liters = volume_cubic_m / 1000
available_liters = volume_liters * (1 - percents_occupied)
print(available_liters)
