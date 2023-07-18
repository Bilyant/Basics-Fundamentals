numbers_count = int(input())
sum_1 = 0
sum_2 = 0
for number in range(1, (numbers_count * 2) + 1):
    if number <= numbers_count:
        current_number = int(input())
        sum_1 += current_number
    elif number > numbers_count / 2:
        current_number = int(input())
        sum_2 += current_number
if sum_1 == sum_2:
    print(f"Yes, sum = {sum_1}")
else:
    difference = abs(sum_1 - sum_2)
    print(f"No, diff = {difference}")
