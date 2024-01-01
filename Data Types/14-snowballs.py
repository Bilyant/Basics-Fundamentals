snowballs = int(input())
best_snowball = 0
best_weight = 0
best_time = 0
best_quality = 0

for snowball in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality
    if value > best_snowball:
        best_snowball = value
        best_weight = weight
        best_time = time
        best_quality = quality

print(f'{best_weight} : {best_time} = {best_snowball:.0f} ({best_quality})')
