number = int(input())
for n in range(1, number + 1):
    digits_sum = 0
    current_digit = n
    while current_digit > 0:
        digits_sum += current_digit % 10
        current_digit //= 10
    is_special = digits_sum == 5 or digits_sum == 7 or digits_sum == 11
    print(f'{n} -> {is_special}')
    