first_sequence = set([int(num) for num in input().split()])
second_sequence = set([int(num) for num in input().split()])
lines = int(input())
are_subset = False

for _ in range(lines):
    line = input().split()
    command = line[0]

    if command == 'Add':
        numbers = [int(num) for num in line[2:]]
        if line[1] == 'First':
            first_sequence = first_sequence.union(set(numbers))
        else:
            second_sequence = second_sequence.union(set(numbers))

    elif command == 'Remove':
        numbers = [int(num) for num in line[2:]]
        if line[1] == 'First':
            first_sequence = first_sequence.difference(set(numbers))
        else:
            second_sequence = second_sequence.difference(set(numbers))

    elif command == 'Check':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            are_subset = True

print(are_subset)
print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
