def get_numbers(string: str):
    numbers = ''
    for char in string:
        if char.isdigit():
            numbers += char
    return int(numbers)


def get_letters(string: str):
    letters = ''
    for char in string:
        if char.isalpha():
            letters += char
    return letters


message = input().split()
result = []

for word in message:
    current_word = []
    first_letter = chr(get_numbers(word))
    letters = get_letters(word)
    current_word.append(first_letter)
    current_word.extend([l for l in letters])
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    result.append(''.join(current_word))

print(' '.join(result))
