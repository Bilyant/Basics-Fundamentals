number = int(input())

for digit in range(1, number + 1):
    digits_sum = 0
    for i in str(digit):
        digits_sum += int(i)

    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        print(f'{digit} -> True')
    else:
        print(f'{digit} -> False')
