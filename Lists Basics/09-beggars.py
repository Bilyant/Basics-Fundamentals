numbers = [int(n) for n in input().split(', ')]
beggars_count = int(input())
beggars_sum = []

for beggar in range(beggars_count):
    current_beggar_sum = 0
    for num in range(beggar, len(numbers), beggars_count):
        current_beggar_sum += numbers[num]
    beggars_sum.append(current_beggar_sum)

print(beggars_sum)
