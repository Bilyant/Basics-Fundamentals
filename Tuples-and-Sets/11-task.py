number_names = int(input())
odd_numbers = set()
even_numbers = set()

for row in range(1, number_names + 1):
    name = input()
    result = sum([ord(ch) for ch in name]) // row
    odd_numbers.add(result) if result % 2 != 0 else even_numbers.add(result)

result = ''

if sum(odd_numbers) == sum(even_numbers):
    union_set = odd_numbers.union(even_numbers)
    result = ', '.join([str(ch) for ch in union_set])
elif sum(odd_numbers) > sum(even_numbers):
    diff_values = odd_numbers.difference(even_numbers)
    result = ', '.join([str(ch) for ch in diff_values])
else:
    sym_difference = odd_numbers.symmetric_difference(even_numbers)
    result = ', '.join([str(ch) for ch in sym_difference])

print(result)
