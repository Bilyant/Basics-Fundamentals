number = int(input())
longest_intersection = set()

for _ in range(number):
    left_part, right_part = input().split('-')
    num_1, num_2 = [int(num) for num in left_part.split(',')]
    num_3, num_4 = [int(num) for num in right_part.split(',')]
    first_set = set(num for num in range(num_1, num_2 + 1))
    second_set = set(num for num in range(num_3, num_4 + 1))
    intersection = first_set.intersection(second_set)
    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection

result = [str(num) for num in longest_intersection]
print(f'Longest intersection is [{", ".join(result)}] with length {len(result)}')
