def valid_index(numbers: [], index: int):
    is_Valid = True
    if index < 0 or index >= len(numbers):
        is_Valid = False
    return is_Valid


def shoot_numbers(numbers: [], line):
    index, power = int(line[1]), int(line[2])
    is_valid = valid_index(numbers, index)
    if is_valid:
        numbers[index] -= power
        if numbers[index] <= 0:
            numbers.pop(index)


def add_numbers(numbers: [], line):
    index, value = int(line[1]), int(line[2])
    is_valid = valid_index(numbers, index)
    if is_valid:
        numbers.insert(index, value)
    else:
        print('Invalid placement!')


def strike_numbers(numbers: [], line: []):
    index, radius = int(line[1]), int(line[2])
    valid_radius = True
    indices = []
    for idx in range((index - radius), (radius * 2) + 2):
        is_valid = valid_index(numbers, idx)
        indices.append(idx)
        if not is_valid:
            valid_radius = False
    if valid_radius:
        for i in range(len(indices)):
            numbers[indices[i]] = None
        numbers = [n for n in numbers if n != None]
    else:
        print('Strike missed!')




numbers = list(map(int, input().split()))
end_command = 'End'
line = input()

commands = {
    'Shoot': shoot_numbers,
    'Add': add_numbers,
    'Strike': strike_numbers,
}

while line != end_command:
    line = line.split()
    command = line[0]
    commands[command](numbers, line)
    line = input()

print('|'.join([str(n) for n in numbers if n != None]))
