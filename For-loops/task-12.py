import sys

numbers_count = int(input())
max_number = -sys.maxsize
sum = 0
for number in range(numbers_count):
    current_number = int(input())
    sum += current_number
    if current_number > max_number:
        max_number = current_number
sum -= max_number
if sum == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(sum - max_number)
    print("No")
    print(f"Diff = {difference}")
    