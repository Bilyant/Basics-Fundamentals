numbers_count = int(input())
min_number = 9223372036854775807
max_number = -9223372036854775807
for number in range(numbers_count):
    current_num = int(input())
    if current_num >= max_number:
        max_number = current_num
    if current_num <= min_number:
        min_number = current_num
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
