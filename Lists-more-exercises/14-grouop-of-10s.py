numbers = list(map(int, input().split(', ')))
max_number = max(numbers)

for group in range(10, max_number + 10, 10):
    current_10 = list(filter(lambda n: n > group - 10 and n <= group, numbers))
    print(f"Group of {group}'s: {current_10}")
