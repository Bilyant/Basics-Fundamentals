usernames = input().split(', ')
valid_usernames = []

for name in usernames:
    is_Valid = True
    if len(name) < 3 or len(name) > 16:
        is_Valid = False

    for char in name:
        if not (char.isalnum() or '-' in char or '_' in char):
            is_Valid = False
            break

    if ' ' in name:
        is_Valid = False

    if is_Valid:
        valid_usernames.append(name)

print('\n'.join(valid_usernames))
