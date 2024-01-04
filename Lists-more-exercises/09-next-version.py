def convert_to_number(numbers: []):
    result = ''
    for n in numbers:
        result += str(n)
    return int(result)


data = list(map(int, input().split('.')))
current_version = convert_to_number(data)
current_version += 1
if current_version > 999:
    print('0.0.0')
else:
    print('.'.join(str(current_version)))
