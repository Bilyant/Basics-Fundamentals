numbers_count = int(input())
sum_odd = 0
sum_even = 0
for number in range(1, numbers_count + 1):
    if number % 2 == 0:
        current_number = int(input())
        sum_even += current_number
    else:
        current_number = int(input())
        sum_odd += current_number
if sum_even == sum_odd:
    print("Yes")
    print(f"Sum = {sum_odd}")
else:
    difference = abs(sum_even - sum_odd)
    print("No")
    print(f"Diff = {difference}")
    