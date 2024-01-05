def swap(numbers, line):
    index_1, index_2 = int(line[1]), int(line[2])
    numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]


def multiply(numbers, line):
    index_1, index_2 = int(line[1]), int(line[2])
    number_1, number_2 = int(numbers[1]), int(numbers[2])
    product = number_1 * number_2
    numbers[index_1] = product

def decrease(numbers, line):
    numbers = [(n-1) for n in numbers]
    return numbers


numbers = list(map(int, input().split()))
end_command = 'end'
line = input()
commands = {
    'swap': swap,
    'multiply': multiply,
    'decrease': decrease,
}

while line != end_command:
    line = line.split()
    command = line[0]
    if command == 'decrease':
        numbers = decrease(numbers, line)
    else:
        commands[command](numbers, line)
    line = input()

print(', '.join([str(n) for n in numbers]))
