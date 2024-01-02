gifts = input().split(' ')
command = input()

while command != 'No Money':
    current_line = command.split(' ')
    current_command = current_line[0]
    gift = current_line[1]

    if current_command == 'OutOfStock':
        if gift in gifts:
            for i in range(len(gifts)):
                if gifts[i] == gift:
                    gifts[i] = 'None'

    elif current_command == 'Required':
        index = int(current_line[2])
        if 0 < index < len(gifts) - 1:
            gifts[index] = gift

    elif current_command == 'JustInCase':
        gifts[-1] = gift

    command = input()

if 'None' in gifts:
    while 'None' in gifts:
        for gift in gifts:
            if gift == 'None':
                gifts.remove('None')

print(' '.join(gifts))
